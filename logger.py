"""
Central logging configuration.
"""

import sys
from pathlib import Path

from loguru import logger

LOG_DIR = Path("logs")
LOG_DIR.mkdir(exist_ok=True)

def configure_logger() -> None:
    logger.remove()
    logger.add(
        sys.stdout,
        level="INFO",
        format="<green>{time:HH:mm:ss}</green> | <level>{level:<8}</level> | {message}",
    )
    logger.add(
        LOG_DIR / "tradepilot.log",
        rotation="10 MB",
        retention=10,
        level="DEBUG",
    )
