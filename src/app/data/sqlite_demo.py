from __future__ import annotations

import sqlite3
from pathlib import Path

from PySide6.QtWidgets import (
    QFormLayout,
    QGroupBox,
    QHBoxLayout,
    QLabel,
    QLineEdit,
    QPushButton,
    QTableWidget,
    QTableWidgetItem,
    QVBoxLayout,
    QWidget,
)


class SqliteDemoWidget(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self._db_path = Path("demo_users.db")

        root = QVBoxLayout(self)
        title = QLabel("SQLite 增删改查")
        title.setStyleSheet("font-size: 18px; font-weight: 700;")
        root.addWidget(title)

        form_group = QGroupBox("用户")
        form = QFormLayout(form_group)
        self.id_input = QLineEdit()
        self.name_input = QLineEdit()
        self.email_input = QLineEdit()
        form.addRow("ID(编辑/删除时必填)", self.id_input)
        form.addRow("姓名", self.name_input)
        form.addRow("邮箱", self.email_input)
        root.addWidget(form_group)

        btns = QHBoxLayout()
        insert_btn = QPushButton("新增")
        update_btn = QPushButton("更新")
        delete_btn = QPushButton("删除")
        reload_btn = QPushButton("刷新")
        insert_btn.clicked.connect(self._insert)
        update_btn.clicked.connect(self._update)
        delete_btn.clicked.connect(self._delete)
        reload_btn.clicked.connect(self._reload)
        btns.addWidget(insert_btn)
        btns.addWidget(update_btn)
        btns.addWidget(delete_btn)
        btns.addWidget(reload_btn)
        btns.addStretch(1)
        root.addLayout(btns)

        self.table = QTableWidget(0, 3)
        self.table.setHorizontalHeaderLabels(["ID", "姓名", "邮箱"])
        root.addWidget(self.table)

        self._init_db()
        self._reload()

    def _connect(self) -> sqlite3.Connection:
        return sqlite3.connect(self._db_path)

    def _init_db(self) -> None:
        with self._connect() as conn:
            conn.execute(
                """
                CREATE TABLE IF NOT EXISTS users (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    email TEXT NOT NULL
                )
                """
            )

    def _insert(self) -> None:
        name = self.name_input.text().strip()
        email = self.email_input.text().strip()
        if not name or not email:
            return
        with self._connect() as conn:
            conn.execute("INSERT INTO users(name, email) VALUES(?, ?)", (name, email))
        self._reload()

    def _update(self) -> None:
        user_id = self.id_input.text().strip()
        name = self.name_input.text().strip()
        email = self.email_input.text().strip()
        if not user_id or not name or not email:
            return
        with self._connect() as conn:
            conn.execute(
                "UPDATE users SET name = ?, email = ? WHERE id = ?",
                (name, email, int(user_id)),
            )
        self._reload()

    def _delete(self) -> None:
        user_id = self.id_input.text().strip()
        if not user_id:
            return
        with self._connect() as conn:
            conn.execute("DELETE FROM users WHERE id = ?", (int(user_id),))
        self._reload()

    def _reload(self) -> None:
        with self._connect() as conn:
            rows = conn.execute("SELECT id, name, email FROM users ORDER BY id").fetchall()

        self.table.setRowCount(len(rows))
        for r, row in enumerate(rows):
            for c, value in enumerate(row):
                self.table.setItem(r, c, QTableWidgetItem(str(value)))
