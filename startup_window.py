"""
Startup configuration window for TradePilot.
"""

from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QFormLayout,
    QGroupBox,
    QLabel,
    QLineEdit,
    QPushButton,
    QSpinBox,
    QStatusBar,
    QVBoxLayout,
    QWidget,
    QMainWindow,
)


class StartupWindow(QMainWindow):
    """Initial startup window."""

    def __init__(self) -> None:
        super().__init__()

        self.setWindowTitle("TradePilot")
        self.resize(650, 520)

        central = QWidget()
        layout = QVBoxLayout(central)

        title = QLabel("TradePilot")
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        title.setStyleSheet("font-size:26px;font-weight:bold;padding:12px;")

        subtitle = QLabel("Configure today's trading session")
        subtitle.setAlignment(Qt.AlignmentFlag.AlignCenter)

        layout.addWidget(title)
        layout.addWidget(subtitle)

        group = QGroupBox("Connection")

        form = QFormLayout(group)

        self.api_key = QLineEdit()
        self.api_secret = QLineEdit()
        self.api_secret.setEchoMode(QLineEdit.EchoMode.Password)

        self.access_token = QLineEdit()

        self.trade_qty = QSpinBox()
        self.trade_qty.setMaximum(1_000_000)
        self.trade_qty.setValue(4800)

        self.max_order_qty = QSpinBox()
        self.max_order_qty.setMaximum(1_000_000)
        self.max_order_qty.setValue(1800)

        form.addRow("API Key", self.api_key)
        form.addRow("API Secret", self.api_secret)
        form.addRow("Today's Access Token", self.access_token)
        form.addRow("Trade Quantity", self.trade_qty)
        form.addRow("Max Order Quantity", self.max_order_qty)

        layout.addWidget(group)

        self.connect_button = QPushButton("CONNECT")
        self.connect_button.setMinimumHeight(42)
        self.connect_button.clicked.connect(self._connect_clicked)

        layout.addWidget(self.connect_button)

        self.status = QStatusBar()
        self.status.showMessage("Waiting to connect...")
        self.setStatusBar(self.status)

        self.setCentralWidget(central)

    def _connect_clicked(self) -> None:
        missing = []

        if not self.api_key.text().strip():
            missing.append("API Key")

        if not self.api_secret.text().strip():
            missing.append("API Secret")

        if not self.access_token.text().strip():
            missing.append("Access Token")

        if missing:
            self.status.showMessage(
                "Missing: " + ", ".join(missing)
            )
            return

        self.status.showMessage(
            "Validation successful. Broker integration coming in Commit 106."
        )
