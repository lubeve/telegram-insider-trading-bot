\"\"\"
Database configuration and setup.
\"\"\"

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from .settings import Settings

# Create settings instance
settings = Settings()

# Create database engine
engine = create_engine(
    settings.DATABASE_URL,
    connect_args={\"check_same_thread\": False} if \"sqlite\" in settings.DATABASE_URL else {}
)

# Create session factory
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Create base class for models
Base = declarative_base()

# Import all models to ensure they are registered with Base
from app.models import *

def get_db():
    \"\"\"Get database session\"\"\"
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()