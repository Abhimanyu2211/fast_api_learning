import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from dotenv import load_dotenv

# 1. Load environment variables from the .env file
load_dotenv()

# 2. Get the database URL from the environment
SQLALCHEMY_DATABASE_URL = os.getenv("DATABASE_URL")

# 3. Engine is the core interface to the database. It manages the actual connection.
# connection pooling is managed here (it keeps a few connections open for speed).
engine = create_engine(SQLALCHEMY_DATABASE_URL)

# 4. SessionLocal is a factory that creates new database sessions.
# Think of a session as a "workspace" for your database operations.
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# 5. Base is a class that our models (like User) will inherit from.
# It tells SQLAlchemy that those classes map to database tables.
Base = declarative_base()

# 6. Dependency: This is a special FastAPI feature.
def get_db():
    db = SessionLocal()
    try:
        # yield gives the database session to the FastAPI route.
        # It essentially "pauses" this function while the route is doing its work.
        yield db
    finally:
        # Once the route is finished, this function resumes and closes the session.
        # This is CRITICAL so we don't leave connections hanging open!
        db.close()
