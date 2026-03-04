"""メイン描画ディスパッチャ"""

import pyxel

from dungeon_dot.constants import TILE_SIZE
from dungeon_dot.domain.dungeon import Dungeon
from dungeon_dot.domain.player import Player
from dungeon_dot.domain.tile import TileType

# タイルごとの色マッピング
TILE_COLORS: dict[TileType, int] = {
    TileType.WALL: 1,
    TileType.FLOOR: 5,
    TileType.STAIRS: 10,
    TileType.TRAP: 8,
}


def draw_dungeon(dungeon: Dungeon) -> None:
    for y, row in enumerate(dungeon.tiles):
        for x, tile in enumerate(row):
            color = TILE_COLORS.get(tile, 0)
            pyxel.rect(x * TILE_SIZE, y * TILE_SIZE, TILE_SIZE, TILE_SIZE, color)


def draw_player(player: Player) -> None:
    pyxel.rect(player.x * TILE_SIZE, player.y * TILE_SIZE, TILE_SIZE, TILE_SIZE, 11)
