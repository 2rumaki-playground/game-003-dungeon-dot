"""シード付き乱数生成"""

import random


class GameRng:
    """再現可能な乱数生成器"""

    def __init__(self, seed: int | None = None) -> None:
        self._rng = random.Random(seed)
        self._seed = seed

    @property
    def seed(self) -> int | None:
        return self._seed

    def randint(self, a: int, b: int) -> int:
        return self._rng.randint(a, b)

    def choice(self, seq: list) -> object:
        return self._rng.choice(seq)

    def shuffle(self, seq: list) -> None:
        self._rng.shuffle(seq)
