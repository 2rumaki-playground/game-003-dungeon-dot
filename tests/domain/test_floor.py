"""フロア進行テスト"""

from dungeon_dot.domain.floor import FloorState


class TestFloorState:
    def test_initial_floor(self) -> None:
        state = FloorState()
        assert state.current_floor == 1
        assert not state.is_final_floor

    def test_advance(self) -> None:
        state = FloorState(current_floor=1, max_floor=3)
        state.advance()
        assert state.current_floor == 2

    def test_cannot_advance_past_max(self) -> None:
        state = FloorState(current_floor=10, max_floor=10)
        assert state.is_final_floor
        state.advance()
        assert state.current_floor == 10
