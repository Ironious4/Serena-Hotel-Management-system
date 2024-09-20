from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Database connection URL
DATABASE_URL = "sqlite:///./hotel.db" 

# Create an engine that connects to the SQLite database
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})

# SessionLocal will be used to create database sessions
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base class that all models will inherit from
Base = declarative_base()

# Dependency to get a session for database operations
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

