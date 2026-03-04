"""ダンジョン生成"""

from dataclasses import dataclass, field

from dungeon_dot.constants import (
    DUNGEON_MAX_ROOM_SIZE,
    DUNGEON_MAX_ROOMS,
    DUNGEON_MIN_ROOM_SIZE,
)
from dungeon_dot.domain.rng import GameRng
from dungeon_dot.domain.tile import TileType


@dataclass
class Room:
    x: int
    y: int
    width: int
    height: int

    @property
    def center(self) -> tuple[int, int]:
        return (self.x + self.width // 2, self.y + self.height // 2)


@dataclass
class Dungeon:
    width: int
    height: int
    tiles: list[list[TileType]] = field(default_factory=list)
    rooms: list[Room] = field(default_factory=list)

    def __post_init__(self) -> None:
        if not self.tiles:
            self.tiles = [[TileType.WALL for _ in range(self.width)] for _ in range(self.height)]


def generate_dungeon(
    width: int,
    height: int,
    rng: GameRng,
    *,
    max_rooms: int = DUNGEON_MAX_ROOMS,
    min_room_size: int = DUNGEON_MIN_ROOM_SIZE,
    max_room_size: int = DUNGEON_MAX_ROOM_SIZE,
) -> Dungeon:
    """ランダムなダンジョンを生成する"""
    dungeon = Dungeon(width=width, height=height)

    for _ in range(max_rooms):
        w = rng.randint(min_room_size, max_room_size)
        h = rng.randint(min_room_size, max_room_size)
        x = rng.randint(1, width - w - 1)
        y = rng.randint(1, height - h - 1)

        room = Room(x=x, y=y, width=w, height=h)

        for ry in range(room.y, room.y + room.height):
            for rx in range(room.x, room.x + room.width):
                dungeon.tiles[ry][rx] = TileType.FLOOR

        if dungeon.rooms:
            prev_cx, prev_cy = dungeon.rooms[-1].center
            new_cx, new_cy = room.center
            for cx in range(min(prev_cx, new_cx), max(prev_cx, new_cx) + 1):
                dungeon.tiles[prev_cy][cx] = TileType.FLOOR
            for cy in range(min(prev_cy, new_cy), max(prev_cy, new_cy) + 1):
                dungeon.tiles[cy][new_cx] = TileType.FLOOR

        dungeon.rooms.append(room)

    return dungeon
