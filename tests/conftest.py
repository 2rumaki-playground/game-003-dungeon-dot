"""共通テストフィクスチャ"""

import pytest

from dungeon_dot.domain.rng import GameRng


@pytest.fixture
def seeded_rng() -> GameRng:
    """再現可能なテスト用RNG（シード=42）"""
    return GameRng(seed=42)
