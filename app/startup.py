"""
Application startup and initialization module.
"""

import asyncio
from telegram import Bot
from telegram.ext import Application, CommandHandler, MessageHandler, filters
from .config.settings import Settings
from .services.telegram_bot import TelegramBotService
from .services.degiro_manager import DegiroConnectionManager
from .services.auth_manager import AuthManager
from .services.portfolio_sync import PortfolioSyncService
from .services.scheduler_service import SchedulerService
from .services.notification_service import NotificationService
from .services.insider_analysis import InsiderAnalysisService
from .services.trading_engine import TradingEngine
from .services.market_data_service import MarketDataService
from .handlers.auth_handlers import AuthHandlers
from .handlers.portfolio_handlers import PortfolioHandlers
from .handlers.admin_handlers import AdminHandlers
from .handlers.status_handlers import StatusHandlers
from .handlers.trading_handlers import TradingHandlers

async def initialize_application():
    """Initialize and configure the application"""
    # Load settings
    settings = Settings()
    
    # Initialize services
    telegram_service = TelegramBotService(settings.TELEGRAM_BOT_TOKEN)
    degiro_manager = DegiroConnectionManager()
    auth_manager = AuthManager()
    portfolio_sync = PortfolioSyncService(degiro_manager)
    scheduler_service = SchedulerService()
    notification_service = NotificationService(telegram_service)
    insider_analysis = InsiderAnalysisService()
    trading_engine = TradingEngine()
    market_data_service = MarketDataService()
    
    # Initialize handlers
    auth_handlers = AuthHandlers(auth_manager, notification_service)
    portfolio_handlers = PortfolioHandlers(portfolio_sync, degiro_manager)
    admin_handlers = AdminHandlers()
    status_handlers = StatusHandlers()
    trading_handlers = TradingHandlers(trading_engine, insider_analysis, market_data_service)
    
    # Create application
    app = Application.builder().token(settings.TELEGRAM_BOT_TOKEN).build()
    
    # Register handlers
    app.add_handler(CommandHandler("start", auth_handlers.start_command))
    app.add_handler(CommandHandler("login", auth_handlers.login_command))
    app.add_handler(CommandHandler("logout", auth_handlers.logout_command))
    app.add_handler(CommandHandler("portfolio", portfolio_handlers.portfolio_command))
    app.add_handler(CommandHandler("sync", portfolio_handlers.sync_command))
    app.add_handler(CommandHandler("status", status_handlers.status_command))
    app.add_handler(CommandHandler("analyze", trading_handlers.analyze_command))
    app.add_handler(CommandHandler("trade", trading_handlers.trade_command))
    app.add_handler(CommandHandler("settings", trading_handlers.settings_command))
    
    # Register admin handlers
    app.add_handler(CommandHandler("admin", admin_handlers.admin_command))
    
    # Start scheduler service
    scheduler_service.start()
    
    return app