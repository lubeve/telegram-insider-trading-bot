\"\"\"
Insider Activities model for the Telegram Insider Trading Bot.
\"\"\"

from sqlalchemy import Column, Integer, String, Float, DateTime, Text, ForeignKey
from sqlalchemy.orm import relationship
from app.config.database import Base
from datetime import datetime


class InsiderActivity(Base):
    \"\"\"Model for storing raw insider trading data collected from various sources.\"\"\"
    
    __tablename__ = "insider_activities"
    
    id = Column(Integer, primary_key=True, index=True)
    transaction_id = Column(String, unique=True, index=True)  # Unique identifier for the transaction
    company_name = Column(String, nullable=False)
    isin = Column(String, index=True)
    ticker = Column(String, index=True)
    insider_name = Column(String, nullable=False)
    insider_title = Column(String)
    transaction_type = Column(String, nullable=False)  # BUY, SELL, OPTION_EXERCISE
    quantity = Column(Float, nullable=False)
    price = Column(Float, nullable=False)
    total_value = Column(Float, nullable=False)
    transaction_date = Column(DateTime, nullable=False)
    filing_date = Column(DateTime)
    source = Column(String, nullable=False)  # e.g., 'DEGIRO', 'SEC', 'Other'
    confidence_score = Column(Float)  # Score from 0.0 to 1.0
    notes = Column(Text)
    created_at = Column(DateTime, default=datetime.utcnow)
    
    # Relationship to trading opportunities
    trading_opportunities = relationship("TradingOpportunity", back_populates="insider_activity")
    
    def __repr__(self):
        return f"<InsiderActivity(id={self.id}, company='{self.company_name}', insider='{self.insider_name}', type='{self.transaction_type}')>"