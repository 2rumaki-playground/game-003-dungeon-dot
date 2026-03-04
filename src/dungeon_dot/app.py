"""Pyxel Appクラス"""

import pyxel

from dungeon_dot.constants import FPS, SCREEN_HEIGHT, SCREEN_TITLE, SCREEN_WIDTH


class App:
    def __init__(self) -> None:
        pyxel.init(SCREEN_WIDTH, SCREEN_HEIGHT, title=SCREEN_TITLE, fps=FPS)
        pyxel.run(self.update, self.draw)

    def update(self) -> None:
        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()

    def draw(self) -> None:
        pyxel.cls(0)
