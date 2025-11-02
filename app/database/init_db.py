"""
Database initialization script for the Telegram Insider Trading Bot.
"""

from sqlalchemy import create_engine
from ..config.database import Base, engine
from ..models.user import User
from ..models.portfolio import Portfolio, Position
from ..models.trade import Trade

def init_db():
    """Initialize the database by creating all tables"""
    # Create all tables
    Base.metadata.create_all(bind=engine)
    print("Database tables created successfully.")

if __name__ == "__main__":
    init_db()