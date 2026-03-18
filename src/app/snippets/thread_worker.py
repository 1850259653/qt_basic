from __future__ import annotations

import time

from PySide6.QtCore import QObject, QThread, Signal


class Worker(QObject):
    progress = Signal(int)
    done = Signal(str)

    def run(self) -> None:
        for i in range(1, 101):
            time.sleep(0.02)
            self.progress.emit(i)
        self.done.emit("ok")


# 用法:
# thread = QThread()
# worker = Worker()
# worker.moveToThread(thread)
# thread.started.connect(worker.run)
# worker.progress.connect(lambda i: print(i))
# worker.done.connect(thread.quit)
# thread.start()
