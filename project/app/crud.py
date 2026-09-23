from sqlalchemy.orm import Session
from . import models, schemas, auth

def get_user_by_username(db: Session, username: str):
    # Look up a user by their exact username
    return db.query(models.User).filter(models.User.username == username).first()

def get_user_by_email(db: Session, email: str):
    # Look up a user by their exact email
    return db.query(models.User).filter(models.User.email == email).first()

def create_user(db: Session, user: schemas.UserCreate):
    # Hash the password before saving
    hashed_password = auth.hash_password(user.password)
    
    # Create the new SQLAlchemy model instance
    db_user = models.User(
        username=user.username,
        email=user.email,
        password_hash=hashed_password
    )
    
    # Add to session and save to MySQL
    try:
        db.add(db_user)
        db.commit()      # Commit saves the transaction
        db.refresh(db_user) # Refresh gets the newly generated ID back
        return db_user
    except Exception as e:
        # Rollback is CRITICAL: if an error happens, we undo the transaction 
        # so the database isn't left in a broken state
        db.rollback()
        raise e
