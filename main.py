"""
TradePilot - Application Entry Point

Milestone 1: Project Bootstrap
"""

import sys

from PySide6.QtWidgets import QApplication, QLabel, QMainWindow
from loguru import logger


class MainWindow(QMainWindow):
    """Temporary main window for Milestone 1."""

    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle("TradePilot v0.1.0")
        self.resize(900, 600)

        label = QLabel(
            "TradePilot\n\n"
            "Milestone 1 - Bootstrap Complete\n\n"
            "Next: Configuration, Logger and Application State"
        )
        label.setStyleSheet("font-size: 18px; padding: 24px;")
        self.setCentralWidget(label)


def configure_logging() -> None:
    """Configure application logging."""
    logger.remove()
    logger.add(
        sys.stdout,
        format="<green>{time:HH:mm:ss}</green> | <level>{level: <8}</level> | {message}",
    )


def main() -> None:
    """Application entry point."""
    configure_logging()
    logger.info("Starting TradePilot")

    app = QApplication(sys.argv)
    app.setApplicationName("TradePilot")

    window = MainWindow()
    window.show()

    logger.info("Application started successfully")

    sys.exit(app.exec())


if __name__ == "__main__":
    main()
