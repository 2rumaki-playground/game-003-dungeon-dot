"""wandb実験トラッキングラッパー"""

from __future__ import annotations

from typing import Any

import wandb


class Tracker:
    """wandbのラッパー。オフラインモードをサポート"""

    def __init__(self, project: str = "dungeon-dot", *, offline: bool = False) -> None:
        self._offline = offline
        mode = "offline" if offline else "online"
        self._run = wandb.init(project=project, mode=mode)

    def log(self, metrics: dict[str, Any]) -> None:
        if self._run is not None:
            self._run.log(metrics)

    def finish(self) -> None:
        if self._run is not None:
            self._run.finish()
            self._run = None
