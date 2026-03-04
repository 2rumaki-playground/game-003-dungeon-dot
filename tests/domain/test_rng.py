"""RNG再現性テスト"""

from dungeon_dot.domain.rng import GameRng


class TestGameRng:
    def test_same_seed_produces_same_sequence(self) -> None:
        rng1 = GameRng(seed=123)
        rng2 = GameRng(seed=123)
        assert [rng1.randint(0, 100) for _ in range(10)] == [
            rng2.randint(0, 100) for _ in range(10)
        ]

    def test_different_seeds_produce_different_sequences(self) -> None:
        rng1 = GameRng(seed=1)
        rng2 = GameRng(seed=2)
        seq1 = [rng1.randint(0, 1000) for _ in range(10)]
        seq2 = [rng2.randint(0, 1000) for _ in range(10)]
        assert seq1 != seq2

    def test_seed_property(self) -> None:
        rng = GameRng(seed=42)
        assert rng.seed == 42
