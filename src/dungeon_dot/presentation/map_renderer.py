"""マップ描画"""

import pyxel

from dungeon_dot.constants import TILE_SIZE
from dungeon_dot.domain.dungeon import Dungeon
from dungeon_dot.domain.tile import TileType


def draw_map(dungeon: Dungeon, *, camera_x: int = 0, camera_y: int = 0) -> None:
    """ダンジョンマップを描画する"""
    for y, row in enumerate(dungeon.tiles):
        for x, tile in enumerate(row):
            sx = x * TILE_SIZE - camera_x
            sy = y * TILE_SIZE - camera_y
            if tile == TileType.WALL:
                pyxel.rect(sx, sy, TILE_SIZE, TILE_SIZE, 1)
            elif tile == TileType.FLOOR:
                pyxel.rect(sx, sy, TILE_SIZE, TILE_SIZE, 5)
            elif tile == TileType.STAIRS:
                pyxel.rect(sx, sy, TILE_SIZE, TILE_SIZE, 10)
