"""タイル定義"""

from enum import IntEnum


class TileType(IntEnum):
    WALL = 0
    FLOOR = 1
    STAIRS = 2
    TRAP = 3
