"""フロア進行"""

from dataclasses import dataclass


@dataclass
class FloorState:
    current_floor: int = 1
    max_floor: int = 10

    @property
    def is_final_floor(self) -> bool:
        return self.current_floor >= self.max_floor

    def advance(self) -> None:
        if not self.is_final_floor:
            self.current_floor += 1
