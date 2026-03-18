from __future__ import annotations

import time

from PySide6.QtCore import QObject, QThread, Signal
from PySide6.QtWidgets import (
    QHBoxLayout,
    QLabel,
    QPushButton,
    QProgressBar,
    QTextEdit,
    QVBoxLayout,
    QWidget,
)


class Worker(QObject):
    progress = Signal(int)
    done = Signal(str)

    def run(self) -> None:
        for i in range(1, 101):
            time.sleep(0.03)
            self.progress.emit(i)
        self.done.emit("后台任务执行完成")


class ThreadingDemoWidget(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.thread: QThread | None = None

        root = QVBoxLayout(self)
        title = QLabel("后台线程与 UI 更新")
        title.setStyleSheet("font-size: 18px; font-weight: 700;")
        root.addWidget(title)

        self.progress = QProgressBar()
        self.progress.setRange(0, 100)
        root.addWidget(self.progress)

        row = QHBoxLayout()
        start_btn = QPushButton("启动后台任务")
        start_btn.clicked.connect(self._start)
        row.addWidget(start_btn)
        row.addStretch(1)
        root.addLayout(row)

        self.log = QTextEdit()
        self.log.setReadOnly(True)
        root.addWidget(self.log)

    def _start(self) -> None:
        if self.thread and self.thread.isRunning():
            self.log.append("任务仍在执行中")
            return

        self.progress.setValue(0)
        self.log.append("开始执行后台任务")

        self.thread = QThread(self)
        worker = Worker()
        worker.moveToThread(self.thread)

        self.thread.started.connect(worker.run)
        worker.progress.connect(self.progress.setValue)
        worker.done.connect(self._on_done)

        worker.done.connect(self.thread.quit)
        worker.done.connect(worker.deleteLater)
        self.thread.finished.connect(self.thread.deleteLater)

        self.thread.start()

    def _on_done(self, message: str) -> None:
        self.log.append(message)
