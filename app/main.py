"""
Main application file for the Telegram Insider Trading Bot.
"""

import asyncio
import logging
from telegram.ext import Application, CommandHandler, MessageHandler, filters
from .config.settings import Settings
from .services.telegram_bot import TelegramBotService
from .services.degiro_manager import DegiroConnectionManager
from .services.trading_manager import TradingManager
from .database.init_db import init_db

# Configure logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

# Initialize settings
settings = Settings()

# Initialize services
telegram_service = TelegramBotService(settings.TELEGRAM_BOT_TOKEN)
degiro_manager = DegiroConnectionManager()
trading_manager = TradingManager()

def start_command(update, context):
    """Handle the /start command"""
    user = update.effective_user
    message = f"Hello {user.first_name}! Welcome to the Insider Trading Bot."
    asyncio.create_task(telegram_service.send_message(
        chat_id=update.effective_chat.id,
        text=message
    ))

def help_command(update, context):
    """Handle the /help command"""
    help_text = """
Available commands:
/start - Start the bot
/help - Show this help message
/portfolio - Show your portfolio status
/trade - Execute a trade
/settings - Configure trading settings
    """
    asyncio.create_task(telegram_service.send_message(
        chat_id=update.effective_chat.id,
        text=help_text
    ))

def portfolio_command(update, context):
    """Handle the /portfolio command"""
    # TODO: Implement portfolio status retrieval
    message = "Portfolio status: Not implemented yet."
    asyncio.create_task(telegram_service.send_message(
        chat_id=update.effective_chat.id,
        text=message
    ))

def trade_command(update, context):
    """Handle the /trade command"""
    # TODO: Implement trade execution
    message = "Trade execution: Not implemented yet."
    asyncio.create_task(telegram_service.send_message(
        chat_id=update.effective_chat.id,
        text=message
    ))

def settings_command(update, context):
    """Handle the /settings command"""
    # TODO: Implement settings configuration
    message = "Trading settings: Not implemented yet."
    asyncio.create_task(telegram_service.send_message(
        chat_id=update.effective_chat.id,
        text=message
    ))

async def main():
    """Main function to start the bot"""
    # Initialize database
    init_db()
    
    # Create the Application instance
    application = Application.builder().token(settings.TELEGRAM_BOT_TOKEN).build()
    
    # Set the application in the telegram service
    telegram_service.set_application(application)
    
    # Register command handlers
    application.add_handler(CommandHandler("start", start_command))
    application.add_handler(CommandHandler("help", help_command))
    application.add_handler(CommandHandler("portfolio", portfolio_command))
    application.add_handler(CommandHandler("trade", trade_command))
    application.add_handler(CommandHandler("settings", settings_command))
    
    # Register message handler for non-command messages
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, help_command))
    
    # Start the bot
    logger.info("Starting Telegram Insider Trading Bot...")
    await application.run_polling()

if __name__ == "__main__":
    asyncio.run(main())