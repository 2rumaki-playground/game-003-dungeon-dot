"""Pyxel Appクラス"""

import pyxel

from dungeon_dot.constants import FPS, SCREEN_HEIGHT, SCREEN_TITLE, SCREEN_WIDTH, TILE_SIZE
from dungeon_dot.domain.dungeon import generate_dungeon
from dungeon_dot.domain.floor import FloorState
from dungeon_dot.domain.player import Player
from dungeon_dot.domain.rng import GameRng
from dungeon_dot.domain.tile import TileType
from dungeon_dot.presentation.hud_renderer import draw_hud
from dungeon_dot.presentation.input_handler import Action, get_action
from dungeon_dot.presentation.renderer import draw_dungeon, draw_player

DUNGEON_WIDTH = SCREEN_WIDTH // TILE_SIZE
DUNGEON_HEIGHT = SCREEN_HEIGHT // TILE_SIZE


class App:
    def __init__(self) -> None:
        self.rng = GameRng()
        self.floor_state = FloorState()
        self.dungeon = generate_dungeon(DUNGEON_WIDTH, DUNGEON_HEIGHT, self.rng)
        self.player = Player()
        self._place_player_in_first_room()

        pyxel.init(SCREEN_WIDTH, SCREEN_HEIGHT, title=SCREEN_TITLE, fps=FPS)
        pyxel.run(self.update, self.draw)

    def _place_player_in_first_room(self) -> None:
        if self.dungeon.rooms:
            cx, cy = self.dungeon.rooms[0].center
            self.player.x = cx
            self.player.y = cy

    def update(self) -> None:
        action = get_action()
        if action == Action.QUIT:
            pyxel.quit()
            return

        dx, dy = 0, 0
        if action == Action.MOVE_UP:
            dy = -1
        elif action == Action.MOVE_DOWN:
            dy = 1
        elif action == Action.MOVE_LEFT:
            dx = -1
        elif action == Action.MOVE_RIGHT:
            dx = 1

        if dx != 0 or dy != 0:
            nx, ny = self.player.x + dx, self.player.y + dy
            if (
                0 <= nx < self.dungeon.width
                and 0 <= ny < self.dungeon.height
                and self.dungeon.tiles[ny][nx] != TileType.WALL
            ):
                self.player.x = nx
                self.player.y = ny

    def draw(self) -> None:
        pyxel.cls(0)
        draw_dungeon(self.dungeon)
        draw_player(self.player)
        draw_hud(self.player, self.floor_state)
