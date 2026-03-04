"""敵タイプ・AI"""

from dataclasses import dataclass


@dataclass
class Enemy:
    x: int
    y: int
    hp: int
    attack: int
    name: str = "Slime"

    @property
    def is_alive(self) -> bool:
        return self.hp > 0

    def take_damage(self, amount: int) -> None:
        self.hp = max(0, self.hp - amount)
