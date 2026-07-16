"""
Shared application state for TradePilot.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime
from typing import Any


@dataclass(slots=True)
class ApplicationState:
    """Single source of truth for runtime state."""

    connected: bool = False
    broker_connected: bool = False

    nifty_spot: float | None = None
    india_vix: float | None = None

    selected_expiry: str | None = None

    strategy_status: str = "INITIALIZING"

    mtm: float = 0.0

    last_updated: datetime = field(default_factory=datetime.now)

    metadata: dict[str, Any] = field(default_factory=dict)

    def touch(self) -> None:
        self.last_updated = datetime.now()

    def update_market(self, *, spot: float | None = None, vix: float | None = None) -> None:
        if spot is not None:
            self.nifty_spot = spot
        if vix is not None:
            self.india_vix = vix
        self.touch()
