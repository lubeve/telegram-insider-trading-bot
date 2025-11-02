\"\"\"
Trading Opportunity model for the Telegram Insider Trading Bot.
\"\"\"

from sqlalchemy import Column, Integer, String, Float, DateTime, Boolean, Text, ForeignKey
from sqlalchemy.orm import relationship
from app.config.database import Base
from datetime import datetime


class TradingOpportunity(Base):
    \"\"\"Model for storing identified trading opportunities from insider activity analysis.\"\"\"
    
    __tablename__ = "trading_opportunities"
    
    id = Column(Integer, primary_key=True, index=True)
    product_id = Column(String, index=True, nullable=False)
    product_name = Column(String, nullable=False)
    isin = Column(String, index=True)
    confidence_score = Column(Float, nullable=False)
    target_price = Column(Float)
    stop_loss_price = Column(Float)
    entry_price = Column(Float)
    quantity = Column(Float)
    trade_type = Column(String, nullable=False)  # BUY or SELL
    detected_at = Column(DateTime, default=datetime.utcnow)
    executed = Column(Boolean, default=False)
    execution_time = Column(DateTime)
    execution_price = Column(Float)
    execution_quantity = Column(Float)
    profit_loss = Column(Float)
    notes = Column(Text)
    
    # Relationship to insider activities
    insider_activity_id = Column(Integer, ForeignKey('insider_activities.id'))
    insider_activity = relationship("InsiderActivity", back_populates="trading_opportunities")
    
    # Relationship to order history
    order_history = relationship("OrderHistory", back_populates="trading_opportunity")
    
    def __repr__(self):
        return f"<TradingOpportunity(id={self.id}, product='{self.product_name}', confidence={self.confidence_score})>"