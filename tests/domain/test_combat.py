"""戦闘テスト"""

from dungeon_dot.domain.combat import resolve_combat
from dungeon_dot.domain.enemy import Enemy
from dungeon_dot.domain.player import Player


class TestCombat:
    def test_player_attacks_enemy(self) -> None:
        player = Player(hp=10, max_hp=10, attack=3)
        enemy = Enemy(x=0, y=0, hp=5, attack=1)
        result = resolve_combat(player, enemy)
        assert result.enemy_damage == 3
        assert enemy.hp == 2

    def test_enemy_counterattacks(self) -> None:
        player = Player(hp=10, max_hp=10, attack=1)
        enemy = Enemy(x=0, y=0, hp=10, attack=2)
        result = resolve_combat(player, enemy)
        assert result.player_damage == 2
        assert player.hp == 8

    def test_enemy_defeated_no_counterattack(self) -> None:
        player = Player(hp=10, max_hp=10, attack=5)
        enemy = Enemy(x=0, y=0, hp=3, attack=99)
        result = resolve_combat(player, enemy)
        assert result.enemy_defeated
        assert result.player_damage == 0
        assert player.hp == 10
