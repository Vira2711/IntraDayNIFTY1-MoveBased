# TradePilot

A professional desktop trading platform for automating discretionary and
systematic options strategies using Zerodha Kite Connect.

> Current Strategy: Intraday NIFTY 1% Move Based Strategy

## Vision

TradePilot is being built as a modular trading platform rather than a
single-purpose bot.

The first implemented strategy will automate an intraday NIFTY options
strategy. The platform is designed so future strategies (Double
Calendar, Iron Fly, Flyogonal, etc.) can be added without modifying the
core trading engine.

## Current Status

Version: **0.1.0**

Milestone: **Foundation**

Completed:

-   [x] Repository Initialized

In Progress:

-   [ ] Application Bootstrap
-   [ ] Configuration Manager
-   [ ] Logger
-   [ ] Application State
-   [ ] Startup UI
-   [ ] Kite Connectivity
-   [ ] Market Data
-   [ ] Instrument Manager

## Technology Stack

  Component       Technology
  --------------- ----------------------
  Language        Python 3.12
  GUI             PySide6
  Broker API      Zerodha Kite Connect
  Market Data     KiteTicker
  Configuration   YAML
  Database        SQLite
  Logging         Loguru
  Charts          PyQtGraph
  Testing         pytest
  Packaging       PyInstaller

## Project Structure

``` text
IntraDayNIFTY1-MoveBased/

app/
broker/
config/
core/
market/
ui/
assets/
docs/
logs/
tests/

main.py
```

## Strategy (Version 1)

### Entry

09:25 IST

Conditions:

-   India VIX strictly between 12 and 20
-   Trade only the first weekly expiry that is more than six calendar
    days away

Orders:

-   Sell 1% OTM Call (Market Order)
-   Sell 1% OTM Put (Market Order)

### Adjustment

If NIFTY rises more than 0.95% from entry: - Buy 100 ITM Call

If NIFTY falls more than 0.95% from entry: - Buy 100 ITM Put

Only one adjustment per trading day.

### Exit

Exit immediately if aggregate MTM \<= -(60 × Trade Quantity).

Otherwise, exit all positions at exactly 15:15 IST.

## Design Principles

-   Strategy Engine never talks directly to Kite.
-   Order Manager is the only module allowed to place orders.
-   Application State is the single source of truth.
-   Every significant action is logged.
-   Every commit should leave the project in a runnable state.

## Roadmap

### Milestone 1

-   Project Bootstrap
-   Configuration
-   Logging
-   Startup UI
-   Kite Connectivity
-   Live Market Data
-   Instrument Manager

### Milestone 2

-   Execution Manager
-   Position Manager
-   MTM Engine

### Milestone 3

-   Entry
-   Adjustment
-   Stop Loss
-   Time Exit

### Milestone 4

-   Replay
-   Recovery
-   Packaging
-   Paper Trading
-   Analytics

## License

Private. Internal use only.
