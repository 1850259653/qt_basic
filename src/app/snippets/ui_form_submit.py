from PySide6.QtWidgets import QHBoxLayout, QLineEdit, QPushButton, QTextEdit, QVBoxLayout, QWidget


class FormSubmitSnippet(QWidget):
    def __init__(self) -> None:
        super().__init__()
        root = QVBoxLayout(self)

        self.input_name = QLineEdit()
        self.output = QTextEdit()
        self.output.setReadOnly(True)

        row = QHBoxLayout()
        submit_btn = QPushButton("提交")
        submit_btn.clicked.connect(self.on_submit)
        row.addWidget(self.input_name)
        row.addWidget(submit_btn)

        root.addLayout(row)
        root.addWidget(self.output)

    def on_submit(self) -> None:
        self.output.setPlainText(f"hello, {self.input_name.text().strip() or 'guest'}")
