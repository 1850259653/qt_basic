from __future__ import annotations

import json
import urllib.error
import urllib.request

from PySide6.QtWidgets import (
    QHBoxLayout,
    QLabel,
    QLineEdit,
    QPushButton,
    QTextEdit,
    QVBoxLayout,
    QWidget,
)


class HttpDemoWidget(QWidget):
    def __init__(self) -> None:
        super().__init__()

        root = QVBoxLayout(self)
        title = QLabel("HTTP API 调用")
        title.setStyleSheet("font-size: 18px; font-weight: 700;")
        root.addWidget(title)

        self.url_input = QLineEdit("https://jsonplaceholder.typicode.com/todos/1")
        root.addWidget(self.url_input)

        row = QHBoxLayout()
        get_btn = QPushButton("GET")
        post_btn = QPushButton("POST")
        get_btn.clicked.connect(self._send_get)
        post_btn.clicked.connect(self._send_post)
        row.addWidget(get_btn)
        row.addWidget(post_btn)
        row.addStretch(1)
        root.addLayout(row)

        self.output = QTextEdit()
        self.output.setReadOnly(True)
        root.addWidget(self.output)

    def _send_get(self) -> None:
        url = self.url_input.text().strip()
        if not url:
            return
        req = urllib.request.Request(url=url, method="GET")
        self._execute(req)

    def _send_post(self) -> None:
        url = self.url_input.text().strip() or "https://jsonplaceholder.typicode.com/posts"
        data = json.dumps({"title": "foo", "body": "bar", "userId": 1}).encode("utf-8")
        req = urllib.request.Request(
            url=url,
            data=data,
            method="POST",
            headers={"Content-Type": "application/json"},
        )
        self._execute(req)

    def _execute(self, req: urllib.request.Request) -> None:
        try:
            with urllib.request.urlopen(req, timeout=8) as resp:
                body = resp.read().decode("utf-8")
                self.output.setPlainText(f"status={resp.status}\n{body}")
        except urllib.error.URLError as exc:
            self.output.setPlainText(f"请求失败: {exc}")
