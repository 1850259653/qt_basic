from __future__ import annotations

from PySide6.QtCore import QTimer
from PySide6.QtWidgets import (
    QCheckBox,
    QHBoxLayout,
    QLabel,
    QMessageBox,
    QPushButton,
    QProgressBar,
    QStackedWidget,
    QVBoxLayout,
    QWidget,
)


class InteractionWidgetsDemo(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self._progress_value = 0

        root = QVBoxLayout(self)

        title = QLabel("对话框 / 进度条 / 分页 / 主题")
        title.setStyleSheet("font-size: 18px; font-weight: 700;")
        root.addWidget(title)

        self.toast_label = QLabel("通知区域")
        self.toast_label.setStyleSheet(
            "padding: 8px; border-radius: 6px; background: #eef4ff; color: #1f3a66;"
        )
        root.addWidget(self.toast_label)

        btn_row = QHBoxLayout()
        dialog_btn = QPushButton("打开对话框")
        dialog_btn.clicked.connect(self._show_dialog)
        toast_btn = QPushButton("显示通知")
        toast_btn.clicked.connect(self._show_toast)
        btn_row.addWidget(dialog_btn)
        btn_row.addWidget(toast_btn)
        btn_row.addStretch(1)
        root.addLayout(btn_row)

        self.progress = QProgressBar()
        self.progress.setRange(0, 100)
        self.progress.setValue(0)
        start_progress_btn = QPushButton("开始进度")
        start_progress_btn.clicked.connect(self._start_progress)
        root.addWidget(self.progress)
        root.addWidget(start_progress_btn)

        self.stack = QStackedWidget()
        self.stack.addWidget(QLabel("Page 1: 主页"))
        self.stack.addWidget(QLabel("Page 2: 配置"))
        self.stack.addWidget(QLabel("Page 3: 日志"))
        page_row = QHBoxLayout()
        for i in range(3):
            btn = QPushButton(f"切换到第{i + 1}页")
            btn.clicked.connect(lambda _, idx=i: self.stack.setCurrentIndex(idx))
            page_row.addWidget(btn)
        page_row.addStretch(1)
        root.addLayout(page_row)
        root.addWidget(self.stack)

        self.theme_toggle = QCheckBox("启用深色风格")
        self.theme_toggle.toggled.connect(self._toggle_theme)
        root.addWidget(self.theme_toggle)
        root.addStretch(1)

        self.timer = QTimer(self)
        self.timer.timeout.connect(self._tick_progress)

    def _show_dialog(self) -> None:
        QMessageBox.information(self, "提示", "这是一个可复用的对话框调用示例。")

    def _show_toast(self) -> None:
        self.toast_label.setText("通知：配置已保存")

    def _start_progress(self) -> None:
        self._progress_value = 0
        self.progress.setValue(0)
        self.timer.start(120)

    def _tick_progress(self) -> None:
        self._progress_value += 5
        self.progress.setValue(self._progress_value)
        if self._progress_value >= 100:
            self.timer.stop()
            self.toast_label.setText("通知：任务完成")

    def _toggle_theme(self, enabled: bool) -> None:
        if enabled:
            self.setStyleSheet(
                "QWidget { background: #1f232a; color: #e6edf3; }"
                "QPushButton { background: #30363d; border: 1px solid #57606a; padding: 6px; }"
            )
        else:
            self.setStyleSheet("")
