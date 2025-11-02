# Telegram Insider Trading Bot

A sophisticated Telegram bot that detects insider trading activities and automatically executes trades through the Degiro API.

## Features

- **Insider Trading Detection**: Monitors and identifies potential insider trading activities
- **Automated Trading**: Automatically executes trades based on detected insider activities
- **Telegram Integration**: Provides real-time updates and control through Telegram
- **Portfolio Management**: Tracks and manages your investment portfolio
- **Risk Management**: Implements trading limits and position sizing controls
- **Real-time Market Data**: Accesses up-to-date market information
- **Trading Opportunity Detection**: Identifies potential profitable trading opportunities

## Architecture

The bot is structured into several key components:

1. **Telegram Bot Service** (`app/services/telegram_bot.py`): Handles all Telegram communication
2. **Degiro Connection Manager** (`app/services/degiro_manager.py`): Manages connections to the Degiro API
3. **Trading Manager** (`app/services/trading_manager.py`): Implements trading logic and risk controls
4. **Database Layer** (`app/database/`): Stores user data, portfolio information, and trade history
5. **Configuration** (`app/config/`): Manages application settings and environment variables

## Requirements

- Python 3.8+
- Telegram Bot API access
- Degiro account credentials
- PostgreSQL database

## Setup

1. Clone the repository:
   ```
   git clone https://github.com/lubeve/telegram-insider-trading-bot.git
   ```

2. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Configure environment variables:
   - Create a `.env` file in the project root
   - Add your Telegram bot token and Degiro credentials

4. Initialize the database:
   ```
   python -m app.database.init_db
   ```

5. Run the bot:
   ```
   python -m app.main
   ```

## Configuration

The bot requires the following environment variables:

- `TELEGRAM_BOT_TOKEN`: Your Telegram bot token from BotFather
- `DEGIRO_USERNAME`: Your Degiro account username
- `DEGIRO_PASSWORD`: Your Degiro account password
- `DATABASE_URL`: Connection string for your PostgreSQL database

## Usage

After starting the bot, interact with it through Telegram using these commands:

- `/start`: Start the bot and get welcome message
- `/help`: Show available commands
- `/portfolio`: View your current portfolio status
- `/trade`: Execute a manual trade
- `/settings`: Configure trading parameters

## Disclaimer

This bot is for educational purposes only. Trading securities involves substantial risk and may not be suitable for all investors. Past performance is not indicative of future results. Always do your own research and consider your risk tolerance before making any investment decisions.

## License

MIT License - see LICENSE file for details.