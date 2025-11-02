\"\"\"
Market Data Cache model for the Telegram Insider Trading Bot.
\"\"\"

from sqlalchemy import Column, Integer, String, Float, DateTime, Text
from app.config.database import Base
from datetime import datetime


class MarketDataCache(Base):
    \"\"\"Model for caching market data to reduce API calls and improve performance.\"\"\"
    
    __tablename__ = "market_data_cache"
    
    id = Column(Integer, primary_key=True, index=True)
    product_id = Column(String, index=True, nullable=False)
    product_name = Column(String, nullable=False)
    isin = Column(String, index=True)
    current_price = Column(Float)
    previous_close = Column(Float)
    open_price = Column(Float)
    high_price = Column(Float)
    low_price = Column(Float)
    volume = Column(Float)
    market_cap = Column(Float)
    pe_ratio = Column(Float)
    dividend_yield = Column(Float)
    sector = Column(String)
    last_updated = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    data_source = Column(String)  # e.g., 'DEGIRO', 'Yahoo Finance', etc.
    raw_data = Column(Text)  # JSON string of raw market data for reference
    
    def __repr__(self):
        return f"<MarketDataCache(id={self.id}, product='{self.product_name}', price={self.current_price})>"