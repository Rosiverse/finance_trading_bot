# Binance Futures Trading Bot (Testnet)

A Python CLI trading bot for placing **MARKET** and **LIMIT** orders on the [Binance Futures Testnet](https://testnet.binancefuture.com).

---

## Prerequisites

- **Python 3.8+** — [Download Python](https://www.python.org/downloads/)
- **Binance Testnet account** — Sign up at [testnet.binancefuture.com](https://testnet.binancefuture.com) and generate your API keys.

---

## Quick Start

The startup script handles everything — creates a virtual environment, installs dependencies, asks for your API keys, and launches the bot.

### Windows

```bash
git clone <your-repo-url>
cd trading_bot
start.bat
```

### Mac / Linux

```bash
git clone <your-repo-url>
cd trading_bot
chmod +x start.sh
./start.sh
```

That's it. The script will:

1. Create a `venv/` virtual environment (if not already present)
2. Install all dependencies from `requirements.txt`
3. Prompt you for your **Binance Testnet API Key** and **Secret** and save them to `.env` (first run only)
4. Start the trading bot

---

## Manual Setup

If you prefer to set things up yourself:

### 1. Create & activate a virtual environment

```bash
python -m venv venv
```

- **Windows:** `venv\Scripts\activate`
- **Mac/Linux:** `source venv/bin/activate`

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Configure environment variables

```bash
cp .env.example .env
```

Open `.env` and fill in your keys:

```
BINANCE_API_KEY=your_testnet_api_key_here
BINANCE_API_SECRET=your_testnet_api_secret_here
```

> **Note:** Never commit your `.env` file. It is already in `.gitignore`.

### 4. Run

```bash
python cli.py
```

---

## Usage

The bot launches an interactive menu where you can:

1. Enter a trading symbol (e.g. `BTCUSDT`)
2. Choose **BUY** or **SELL**
3. Choose **MARKET** or **LIMIT** order type
4. Enter quantity (and price for LIMIT orders)
5. Review and confirm the order

---

## Project Structure

```
trading_bot/
├── start.bat               # One-click setup & launch (Windows)
├── start.sh                # One-click setup & launch (Mac/Linux)
├── cli.py                  # Entry point — interactive CLI menu
├── bot/
│   ├── client.py           # Binance API client & HMAC-SHA256 signing
│   ├── orders.py           # Order validation & placement
│   ├── validators.py       # Input validation helpers
│   └── logging_config.py   # Rotating file logger setup
├── logs/                   # Runtime logs (auto-created)
├── requirements.txt        # Python dependencies
├── .env.example            # Template for environment variables
├── .gitignore
└── README.md
```

---

## Logs

All API requests and errors are logged to `logs/trading_bot.log` (auto-rotated at 5 MB, keeps 2 backups).

---

## License

MIT
