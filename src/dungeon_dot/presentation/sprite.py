"""スプライトユーティリティ"""

from dataclasses import dataclass


@dataclass
class SpriteSheet:
    image_bank: int
    tile_width: int
    tile_height: int

    def get_uv(self, index: int, *, columns: int = 16) -> tuple[int, int]:
        """スプライトインデックスからUV座標を計算"""
        u = (index % columns) * self.tile_width
        v = (index // columns) * self.tile_height
        return (u, v)
