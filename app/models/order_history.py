\"\"\"
Order History model for the Telegram Insider Trading Bot.
\"\"\"

from sqlalchemy import Column, Integer, String, Float, DateTime, Text, ForeignKey
from sqlalchemy.orm import relationship
from app.config.database import Base
from datetime import datetime


class OrderHistory(Base):
    \"\"\"Model for tracking all executed orders for reporting and analysis.\"\"\"
    
    __tablename__ = "order_history"
    
    id = Column(Integer, primary_key=True, index=True)
    order_id = Column(String, unique=True, index=True, nullable=False)  # From broker
    product_id = Column(String, index=True, nullable=False)
    product_name = Column(String, nullable=False)
    isin = Column(String, index=True)
    order_type = Column(String, nullable=False)  # BUY or SELL
    quantity = Column(Float, nullable=False)
    price = Column(Float, nullable=False)
    total_value = Column(Float, nullable=False)
    status = Column(String, nullable=False)  # FILLED, REJECTED, CANCELLED
    placed_at = Column(DateTime, default=datetime.utcnow)
    executed_at = Column(DateTime)
    broker = Column(String, default="DEGIRO")
    trading_opportunity_id = Column(Integer, ForeignKey('trading_opportunities.id'))
    notes = Column(Text)
    
    # Relationship to trading opportunity
    trading_opportunity = relationship("TradingOpportunity", back_populates="order_history")
    
    def __repr__(self):
        return f"<OrderHistory(id={self.id}, product='{self.product_name}', status='{self.status}')>"