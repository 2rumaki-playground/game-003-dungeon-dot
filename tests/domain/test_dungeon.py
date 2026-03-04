"""ダンジョン生成テスト"""

from dungeon_dot.domain.dungeon import generate_dungeon
from dungeon_dot.domain.rng import GameRng
from dungeon_dot.domain.tile import TileType


class TestDungeonGeneration:
    def test_generates_rooms(self, seeded_rng: GameRng) -> None:
        dungeon = generate_dungeon(30, 20, seeded_rng)
        assert len(dungeon.rooms) > 0

    def test_rooms_have_floor_tiles(self, seeded_rng: GameRng) -> None:
        dungeon = generate_dungeon(30, 20, seeded_rng)
        floor_count = sum(1 for row in dungeon.tiles for tile in row if tile == TileType.FLOOR)
        assert floor_count > 0

    def test_deterministic_with_same_seed(self) -> None:
        d1 = generate_dungeon(30, 20, GameRng(seed=99))
        d2 = generate_dungeon(30, 20, GameRng(seed=99))
        assert d1.tiles == d2.tiles

    def test_dungeon_dimensions(self, seeded_rng: GameRng) -> None:
        dungeon = generate_dungeon(40, 25, seeded_rng)
        assert dungeon.width == 40
        assert dungeon.height == 25
        assert len(dungeon.tiles) == 25
        assert len(dungeon.tiles[0]) == 40
