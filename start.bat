@echo off
setlocal enabledelayedexpansion
title Binance Futures Trading Bot - Setup ^& Launch
echo ============================================
echo   Binance Futures Trading Bot (Testnet)
echo ============================================
echo.

REM --- Step 1: Create virtual environment if it doesn't exist ---
if not exist "venv" (
    echo [1/4] Creating virtual environment...
    python -m venv venv
    if errorlevel 1 (
        echo ERROR: Failed to create virtual environment. Make sure Python 3.8+ is installed.
        pause
        exit /b 1
    )
    echo       Done.
) else (
    echo [1/4] Virtual environment already exists. Skipping.
)

REM --- Step 2: Activate virtual environment ---
echo [2/4] Activating virtual environment...
call venv\Scripts\activate.bat

REM --- Step 3: Install dependencies ---
echo [3/4] Installing dependencies...
pip install -r requirements.txt --quiet
if errorlevel 1 (
    echo ERROR: Failed to install dependencies.
    pause
    exit /b 1
)
echo       Done.

REM --- Step 4: Configure .env if it doesn't exist ---
if not exist ".env" (
    echo [4/4] Setting up environment variables...
    echo.
    echo       Get your API keys from: https://testnet.binancefuture.com
    echo.
    set /p API_KEY="       Enter your BINANCE_API_KEY: "
    set /p API_SECRET="       Enter your BINANCE_API_SECRET: "
    (
        echo # Binance Testnet API credentials
        echo BINANCE_API_KEY=!API_KEY!
        echo BINANCE_API_SECRET=!API_SECRET!
    ) > .env
    echo       .env file created.
) else (
    echo [4/4] .env file already exists. Skipping.
)

echo.
echo ============================================
echo   Setup complete! Starting the bot...
echo ============================================
echo.

python cli.py
pause
