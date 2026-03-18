from __future__ import annotations

import json
from pathlib import Path


def test_json_roundtrip(tmp_path: Path) -> None:
    path = tmp_path / "demo_data.json"
    payload = {"name": "Alice", "email": "alice@example.com"}

    path.write_text(json.dumps(payload, ensure_ascii=False), "utf-8")
    loaded = json.loads(path.read_text("utf-8"))

    assert loaded == payload
