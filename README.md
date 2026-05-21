# Binance Futures Trading Bot (Testnet)

A simple Python-based interactive terminal application for placing MARKET and LIMIT orders on the Binance Futures Testnet (USDT-M). Built with `requests`, `rich`, and `questionary`.

## Features
- Connects securely to `https://testnet.binancefuture.com`.
- Reads `BINANCE_API_KEY` and `BINANCE_API_SECRET` from environment variables without exposing them.
- Uses HMAC-SHA256 required by Binance for authenticated endpoints.
- Interactive CLI menu that prompts for symbol, side, type, quantity, and limit price.
- Logs all raw API details and errors into `logs/trading_bot.log`.
- Clear try-except wrapping to handle invalid inputs or Binance API errors.

## Project Structure
- `cli.py`: Main execution script with the interactive menu.
- `bot/client.py`: Handles HTTP requests and Binance signature creation.
- `bot/orders.py`: Validates formats and dispatches commands to the client.
- `bot/logging_config.py`: File logger initialization.

## Environment Setup

1. Clone or navigate to the directory.
2. Install standard requirements:
   ```bash
   pip install -r requirements.txt
   ```
3. Set your environment variables in a `.env` file in the same directory:
   ```env
   BINANCE_API_KEY=<your_testnet_api_key>
   BINANCE_API_SECRET=<your_testnet_api_secret>
   ```

## Running the Bot

Start the interactive terminal and follow the prompts:
```bash
python cli.py
```
