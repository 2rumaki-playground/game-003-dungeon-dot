"""HUD描画"""

import pyxel

from dungeon_dot.domain.floor import FloorState
from dungeon_dot.domain.player import Player


def draw_hud(player: Player, floor_state: FloorState) -> None:
    """HP・フロア表示"""
    pyxel.text(2, 2, f"HP:{player.hp}/{player.max_hp}", 7)
    pyxel.text(2, 10, f"F{floor_state.current_floor}", 7)
