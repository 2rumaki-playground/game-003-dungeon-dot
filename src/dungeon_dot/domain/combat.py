"""戦闘処理"""

from dataclasses import dataclass

from dungeon_dot.domain.enemy import Enemy
from dungeon_dot.domain.player import Player


@dataclass
class CombatResult:
    player_damage: int
    enemy_damage: int
    enemy_defeated: bool


def resolve_combat(player: Player, enemy: Enemy) -> CombatResult:
    """1ターン分の戦闘を解決する"""
    enemy_damage = player.attack
    enemy.take_damage(enemy_damage)

    player_damage = 0
    if enemy.is_alive:
        player_damage = enemy.attack
        player.take_damage(player_damage)

    return CombatResult(
        player_damage=player_damage,
        enemy_damage=enemy_damage,
        enemy_defeated=not enemy.is_alive,
    )
