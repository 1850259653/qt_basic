from __future__ import annotations

import sqlite3
from pathlib import Path


def test_sqlite_insert_and_query(tmp_path: Path) -> None:
    db = tmp_path / "users.db"

    with sqlite3.connect(db) as conn:
        conn.execute(
            "CREATE TABLE users(id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, email TEXT)"
        )
        conn.execute(
            "INSERT INTO users(name, email) VALUES(?, ?)",
            ("Bob", "bob@example.com"),
        )
        rows = conn.execute("SELECT name, email FROM users").fetchall()

    assert rows == [("Bob", "bob@example.com")]
