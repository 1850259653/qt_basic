from __future__ import annotations

import sqlite3
from pathlib import Path


class UserRepo:
    def __init__(self, db_path: Path) -> None:
        self.db_path = db_path
        self.init_db()

    def _connect(self) -> sqlite3.Connection:
        return sqlite3.connect(self.db_path)

    def init_db(self) -> None:
        with self._connect() as conn:
            conn.execute(
                "CREATE TABLE IF NOT EXISTS users(id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, email TEXT)"
            )

    def insert(self, name: str, email: str) -> None:
        with self._connect() as conn:
            conn.execute("INSERT INTO users(name, email) VALUES(?, ?)", (name, email))

    def list_all(self) -> list[tuple[int, str, str]]:
        with self._connect() as conn:
            return conn.execute("SELECT id, name, email FROM users ORDER BY id").fetchall()
