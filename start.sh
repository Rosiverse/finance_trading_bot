#!/usr/bin/env bash
set -e

echo "============================================"
echo "  Binance Futures Trading Bot (Testnet)"
echo "============================================"
echo

# --- Step 1: Create virtual environment if it doesn't exist ---
if [ ! -d "venv" ]; then
    echo "[1/4] Creating virtual environment..."
    python3 -m venv venv
    echo "      Done."
else
    echo "[1/4] Virtual environment already exists. Skipping."
fi

# --- Step 2: Activate virtual environment ---
echo "[2/4] Activating virtual environment..."
source venv/bin/activate

# --- Step 3: Install dependencies ---
echo "[3/4] Installing dependencies..."
pip install -r requirements.txt --quiet
echo "      Done."

# --- Step 4: Configure .env if it doesn't exist ---
if [ ! -f ".env" ]; then
    echo "[4/4] Setting up environment variables..."
    echo
    echo "      Get your API keys from: https://testnet.binancefuture.com"
    echo
    read -p "      Enter your BINANCE_API_KEY: " API_KEY
    read -p "      Enter your BINANCE_API_SECRET: " API_SECRET

    cat > .env <<EOF
# Binance Testnet API credentials
BINANCE_API_KEY=${API_KEY}
BINANCE_API_SECRET=${API_SECRET}
EOF

    echo "      .env file created."
else
    echo "[4/4] .env file already exists. Skipping."
fi

echo
echo "============================================"
echo "  Setup complete! Starting the bot..."
echo "============================================"
echo

python cli.py
