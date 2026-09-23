from sqlalchemy import Column, Integer, String, TIMESTAMP
from sqlalchemy.sql import func
from .database import Base

class User(Base):
    # This tells SQLAlchemy the name of the table in MySQL
    __tablename__ = "users"

    # Primary Key - uniquely identifies each row
    id = Column(Integer, primary_key=True, index=True)
    
    # Username must be unique and cannot be empty (nullable=False)
    username = Column(String(50), unique=True, index=True, nullable=False)
    
    # Email must be unique and cannot be empty
    email = Column(String(100), unique=True, index=True, nullable=False)
    
    # We store the hashed password, never the real password!
    password_hash = Column(String(255), nullable=False)
    
    # Automatically records when the user was created
    # func.now() pulls the current timestamp from the database
    created_at = Column(TIMESTAMP, server_default=func.now())
