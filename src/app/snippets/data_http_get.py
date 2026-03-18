from __future__ import annotations

import urllib.error
import urllib.request


def http_get_text(url: str, timeout: int = 8) -> str:
    req = urllib.request.Request(url=url, method="GET")
    try:
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            return resp.read().decode("utf-8")
    except urllib.error.URLError as exc:
        return f"request failed: {exc}"
