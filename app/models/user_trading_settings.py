\"\"\"
User Trading Settings model for the Telegram Insider Trading Bot.
\"\"\"

from sqlalchemy import Column, Integer, String, Float, DateTime, Boolean
from app.config.database import Base
from datetime import datetime


class UserTradingSettings(Base):
    \"\"\"Model for storing user-specific trading configuration settings.\"\"\"
    
    __tablename__ = "user_trading_settings"
    
    id = Column(Integer, primary_key=True, index=True)
    max_position_size = Column(Float, default=10000.0)
    max_daily_trades = Column(Integer, default=3)
    risk_tolerance = Column(Float, default=0.02)  # 2% of portfolio per trade
    preferred_exchange = Column(String, default="DEGIRO")
    auto_execute_trades = Column(Boolean, default=False)
    insider_confidence_threshold = Column(Float, default=0.7)  # Minimum confidence score to consider
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    def __repr__(self):
        return f"<UserTradingSettings(id={self.id}, max_position_size={self.max_position_size}, auto_execute={self.auto_execute_trades})>"