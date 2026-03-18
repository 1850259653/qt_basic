from __future__ import annotations

import json
from pathlib import Path

from PySide6.QtWidgets import (
    QFormLayout,
    QGroupBox,
    QHBoxLayout,
    QLabel,
    QLineEdit,
    QPushButton,
    QTextEdit,
    QVBoxLayout,
    QWidget,
)


class JsonDemoWidget(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self._path = Path("demo_data.json")

        root = QVBoxLayout(self)
        title = QLabel("JSON 文件读写")
        title.setStyleSheet("font-size: 18px; font-weight: 700;")
        root.addWidget(title)

        group = QGroupBox("表单")
        form = QFormLayout(group)
        self.name_input = QLineEdit()
        self.email_input = QLineEdit()
        form.addRow("姓名", self.name_input)
        form.addRow("邮箱", self.email_input)
        root.addWidget(group)

        btns = QHBoxLayout()
        save_btn = QPushButton("保存到 JSON")
        load_btn = QPushButton("从 JSON 读取")
        save_btn.clicked.connect(self._save)
        load_btn.clicked.connect(self._load)
        btns.addWidget(save_btn)
        btns.addWidget(load_btn)
        btns.addStretch(1)
        root.addLayout(btns)

        self.output = QTextEdit()
        self.output.setReadOnly(True)
        root.addWidget(self.output)

    def _save(self) -> None:
        payload = {
            "name": self.name_input.text().strip(),
            "email": self.email_input.text().strip(),
        }
        try:
            self._path.write_text(json.dumps(payload, ensure_ascii=False, indent=2), "utf-8")
            self.output.setPlainText(f"保存成功: {self._path.resolve()}\n{json.dumps(payload, ensure_ascii=False, indent=2)}")
        except OSError as exc:
            self.output.setPlainText(f"保存失败: {exc}")

    def _load(self) -> None:
        try:
            text = self._path.read_text("utf-8")
            data = json.loads(text)
        except FileNotFoundError:
            self.output.setPlainText("未找到 demo_data.json，请先保存")
            return
        except json.JSONDecodeError as exc:
            self.output.setPlainText(f"JSON 解析失败: {exc}")
            return

        self.name_input.setText(str(data.get("name", "")))
        self.email_input.setText(str(data.get("email", "")))
        self.output.setPlainText(f"读取成功:\n{text}")
