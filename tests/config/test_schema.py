"""設定スキーマテスト"""

from dungeon_dot.config.schema import AppConfig, GameConfig, RenderingConfig, TrackingConfig


class TestAppConfig:
    def test_default_values(self) -> None:
        cfg = AppConfig()
        assert cfg.game.starting_hp == 10
        assert cfg.rendering.screen_width == 160
        assert cfg.tracking.enabled is False

    def test_custom_game_config(self) -> None:
        cfg = AppConfig(game=GameConfig(starting_hp=20, max_rooms=10))
        assert cfg.game.starting_hp == 20
        assert cfg.game.max_rooms == 10

    def test_rendering_defaults(self) -> None:
        cfg = RenderingConfig()
        assert cfg.fps == 30
        assert cfg.tile_size == 8

    def test_tracking_offline(self) -> None:
        cfg = TrackingConfig(enabled=True, offline=True)
        assert cfg.offline
