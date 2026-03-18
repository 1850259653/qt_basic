from __future__ import annotations

from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QFormLayout,
    QGridLayout,
    QGroupBox,
    QHBoxLayout,
    QLabel,
    QLineEdit,
    QPushButton,
    QTextEdit,
    QVBoxLayout,
    QWidget,
)


class BasicWidgetsDemo(QWidget):
    def __init__(self) -> None:
        super().__init__()
        root = QVBoxLayout(self)

        title = QLabel("基础控件与布局示例")
        title.setStyleSheet("font-size: 18px; font-weight: 700;")
        root.addWidget(title)

        root.addWidget(self._build_form_group())
        root.addWidget(self._build_layout_group())
        root.addStretch(1)

    def _build_form_group(self) -> QGroupBox:
        group = QGroupBox("输入与按钮")
        layout = QFormLayout(group)

        self.name_input = QLineEdit()
        self.role_input = QLineEdit()
        self.output = QTextEdit()
        self.output.setReadOnly(True)
        self.output.setPlaceholderText("点击按钮后输出结果")

        submit_btn = QPushButton("提交")
        clear_btn = QPushButton("清空")

        submit_btn.clicked.connect(self._on_submit)
        clear_btn.clicked.connect(self._on_clear)

        btn_row = QHBoxLayout()
        btn_row.addWidget(submit_btn)
        btn_row.addWidget(clear_btn)
        btn_row.addStretch(1)

        layout.addRow("姓名", self.name_input)
        layout.addRow("角色", self.role_input)
        layout.addRow(btn_row)
        layout.addRow("输出", self.output)
        return group

    def _build_layout_group(self) -> QGroupBox:
        group = QGroupBox("布局速览")
        grid = QGridLayout(group)

        samples = [
            ("QHBoxLayout", "水平排列组件"),
            ("QVBoxLayout", "垂直排列组件"),
            ("QGridLayout", "网格对齐字段"),
            ("QFormLayout", "表单输入场景"),
        ]
        for index, (name, desc) in enumerate(samples):
            row = index // 2
            col = index % 2
            card = QLabel(f"{name}\n{desc}")
            card.setAlignment(Qt.AlignCenter)
            card.setStyleSheet(
                "border: 1px solid #c9d1d9; border-radius: 8px; padding: 10px;"
            )
            grid.addWidget(card, row, col)
        return group

    def _on_submit(self) -> None:
        name = self.name_input.text().strip() or "匿名"
        role = self.role_input.text().strip() or "未填写"
        self.output.setPlainText(f"提交成功\nname={name}\nrole={role}")

    def _on_clear(self) -> None:
        self.name_input.clear()
        self.role_input.clear()
        self.output.clear()
