"""
Application settings and configuration management.
"""

import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

class Settings:
    """Application settings class"""
    
    def __init__(self):
        # Telegram Bot Settings
        self.TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
        self.TELEGRAM_ADMIN_ID = os.getenv("TELEGRAM_ADMIN_ID")
        
        # Database Settings
        self.DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./insider_bot.db")
        
        # Degiro Settings
        self.DEGIRO_USERNAME = os.getenv("DEGIRO_USERNAME")
        self.DEGIRO_PASSWORD = os.getenv("DEGIRO_PASSWORD")
        
        # Trading Settings
        self.TRADING_ENABLED = os.getenv("TRADING_ENABLED", "False").lower() == "true"
        self.MAX_POSITION_SIZE = float(os.getenv("MAX_POSITION_SIZE", "10000.0"))
        self.MAX_DAILY_TRADES = int(os.getenv("MAX_DAILY_TRADES", "3"))
        
        # Market Data Settings
        self.MARKET_DATA_REFRESH_INTERVAL = int(os.getenv("MARKET_DATA_REFRESH_INTERVAL", "300"))  # seconds
        
        # Logging Settings
        self.LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")
        
        # Validation
        self._validate_settings()
    
    def _validate_settings(self):
        """Validate required settings"""
        if not self.TELEGRAM_BOT_TOKEN:
            raise ValueError("TELEGRAM_BOT_TOKEN environment variable is required")
        
        if not self.DATABASE_URL:
            raise ValueError("DATABASE_URL environment variable is required")

# Create a singleton instance
settings = Settings()