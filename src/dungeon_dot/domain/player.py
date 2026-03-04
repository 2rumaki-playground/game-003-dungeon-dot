"""プレイヤー状態"""

from dataclasses import dataclass

from dungeon_dot.constants import PLAYER_INITIAL_ATTACK, PLAYER_INITIAL_HP


@dataclass
class Player:
    x: int = 0
    y: int = 0
    hp: int = PLAYER_INITIAL_HP
    max_hp: int = PLAYER_INITIAL_HP
    attack: int = PLAYER_INITIAL_ATTACK

    @property
    def is_alive(self) -> bool:
        return self.hp > 0

    def take_damage(self, amount: int) -> None:
        self.hp = max(0, self.hp - amount)

    def heal(self, amount: int) -> None:
        self.hp = min(self.max_hp, self.hp + amount)
