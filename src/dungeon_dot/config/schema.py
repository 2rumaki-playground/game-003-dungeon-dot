"""Hydra Structured Configデータクラス"""

from dataclasses import dataclass, field


@dataclass
class GameConfig:
    starting_hp: int = 10
    base_attack: int = 1
    max_rooms: int = 6
    dungeon_width: int = 20
    dungeon_height: int = 15
    max_floor: int = 10


@dataclass
class RenderingConfig:
    screen_width: int = 160
    screen_height: int = 120
    tile_size: int = 8
    fps: int = 30


@dataclass
class TrackingConfig:
    enabled: bool = False
    project: str = "dungeon-dot"
    offline: bool = True


@dataclass
class AppConfig:
    game: GameConfig = field(default_factory=GameConfig)
    rendering: RenderingConfig = field(default_factory=RenderingConfig)
    tracking: TrackingConfig = field(default_factory=TrackingConfig)
