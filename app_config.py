"""
Configuration manager for TradePilot.
"""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

import yaml


@dataclass(slots=True)
class BrokerConfig:
    api_key: str
    api_secret: str
    access_token: str


@dataclass(slots=True)
class TradingConfig:
    trade_quantity: int
    max_order_quantity: int


@dataclass(slots=True)
class AppConfig:
    name: str
    version: str
    broker: BrokerConfig
    trading: TradingConfig


class ConfigManager:
    """Loads application configuration."""

    def __init__(self, config_path: Path):
        self._config_path = config_path

    def load(self) -> AppConfig:
        with self._config_path.open("r", encoding="utf-8") as f:
            data = yaml.safe_load(f)

        return AppConfig(
            name=data["app"]["name"],
            version=data["app"]["version"],
            broker=BrokerConfig(**data["broker"]),
            trading=TradingConfig(**data["trading"]),
        )
