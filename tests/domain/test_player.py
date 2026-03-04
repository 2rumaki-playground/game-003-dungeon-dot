"""プレイヤーテスト"""

from dungeon_dot.domain.player import Player


class TestPlayer:
    def test_initial_state(self) -> None:
        player = Player()
        assert player.hp == player.max_hp
        assert player.is_alive

    def test_take_damage(self) -> None:
        player = Player(hp=10, max_hp=10)
        player.take_damage(3)
        assert player.hp == 7

    def test_take_damage_does_not_go_below_zero(self) -> None:
        player = Player(hp=5, max_hp=10)
        player.take_damage(100)
        assert player.hp == 0
        assert not player.is_alive

    def test_heal(self) -> None:
        player = Player(hp=5, max_hp=10)
        player.heal(3)
        assert player.hp == 8

    def test_heal_does_not_exceed_max(self) -> None:
        player = Player(hp=9, max_hp=10)
        player.heal(5)
        assert player.hp == 10
