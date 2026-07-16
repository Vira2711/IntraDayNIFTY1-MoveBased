"""
Application bootstrap.
"""

from pathlib import Path

from config.app_config import ConfigManager
from core.logger import configure_logger
from core.state import ApplicationState


class Bootstrap:
    """Initializes the application."""

    def __init__(self):
        self.state = ApplicationState()

    def initialize(self):
        configure_logger()

        config = ConfigManager(
            Path("config/config.yaml")
        ).load()

        self.state.metadata["config"] = config

        return self.state
