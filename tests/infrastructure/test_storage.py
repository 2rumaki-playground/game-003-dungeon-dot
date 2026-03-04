"""ストレージテスト"""

from pathlib import Path

from dungeon_dot.infrastructure.storage import load_game, save_game


class TestStorage:
    def test_save_and_load_round_trip(self, tmp_path: Path) -> None:
        data = {"floor": 3, "hp": 8, "items": ["potion"]}
        path = tmp_path / "save.json"
        save_game(data, path)
        loaded = load_game(path)
        assert loaded == data

    def test_load_nonexistent_returns_none(self, tmp_path: Path) -> None:
        path = tmp_path / "nonexistent.json"
        assert load_game(path) is None
