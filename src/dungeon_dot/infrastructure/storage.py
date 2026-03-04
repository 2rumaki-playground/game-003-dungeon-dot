"""セーブ/ロード"""

from __future__ import annotations

import json
from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from pathlib import Path


def save_game(data: dict[str, Any], path: Path) -> None:
    """ゲーム状態をJSONファイルに保存"""
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")


def load_game(path: Path) -> dict[str, Any] | None:
    """JSONファイルからゲーム状態を読み込み。ファイルがなければNone"""
    if not path.exists():
        return None
    return json.loads(path.read_text(encoding="utf-8"))
