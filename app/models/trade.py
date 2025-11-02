"""
Trade model for the Telegram Insider Trading Bot.
"""

from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey, Enum
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from ..config.database import Base
import enum

class TradeType(enum.Enum):
    """Trade type enumeration"""
    BUY = "buy"
    SELL = "sell"

class TradeStatus(enum.Enum):
    """Trade status enumeration"""
    PENDING = "pending"
    EXECUTED = "executed"
    FAILED = "failed"
    CANCELLED = "cancelled"

class Trade(Base):
    """Trade model representing a trading transaction"""
    
    __tablename__ = "trades"
    
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    product_id = Column(String, nullable=False)
    product_name = Column(String, nullable=False)
    trade_type = Column(Enum(TradeType), nullable=False)
    quantity = Column(Float, nullable=False)
    price = Column(Float, nullable=False)
    total_value = Column(Float, nullable=False)
    status = Column(Enum(TradeStatus), default=TradeStatus.PENDING)
    degiro_order_id = Column(String, nullable=True)
    created_at = Column(DateTime, default=func.now())
    executed_at = Column(DateTime, nullable=True)
    
    # Relationships
    user = relationship("User", back_populates="trades")