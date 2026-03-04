"""入力マッピング"""

from enum import Enum, auto

import pyxel


class Action(Enum):
    NONE = auto()
    MOVE_UP = auto()
    MOVE_DOWN = auto()
    MOVE_LEFT = auto()
    MOVE_RIGHT = auto()
    QUIT = auto()


def get_action() -> Action:
    """現在の入力からアクションを返す"""
    if pyxel.btnp(pyxel.KEY_UP) or pyxel.btnp(pyxel.KEY_W):
        return Action.MOVE_UP
    if pyxel.btnp(pyxel.KEY_DOWN) or pyxel.btnp(pyxel.KEY_S):
        return Action.MOVE_DOWN
    if pyxel.btnp(pyxel.KEY_LEFT) or pyxel.btnp(pyxel.KEY_A):
        return Action.MOVE_LEFT
    if pyxel.btnp(pyxel.KEY_RIGHT) or pyxel.btnp(pyxel.KEY_D):
        return Action.MOVE_RIGHT
    if pyxel.btnp(pyxel.KEY_Q):
        return Action.QUIT
    return Action.NONE
