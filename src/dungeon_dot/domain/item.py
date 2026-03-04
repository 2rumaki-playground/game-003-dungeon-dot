"""アイテム"""

from dataclasses import dataclass
from enum import Enum, auto


class ItemType(Enum):
    POTION = auto()
    WEAPON = auto()
    KEY = auto()


@dataclass
class Item:
    item_type: ItemType
    name: str
    value: int
