"""Database configuration module."""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import NullPool
from typing import Generator
from core.constants import DATABASE_URL

# Create engine with the appropriate driver
engine = create_engine(
    DATABASE_URL,
    poolclass=NullPool,  # Disable connection pooling for CockroachDB
    echo=False,
)

# Create session factory
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db() -> Generator:
    """
    Get a database session.

    Yields:
        Session: A SQLAlchemy session object.
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
