from passlib.context import CryptContext

# This sets up our hashing tool using the bcrypt algorithm
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hash_password(password: str) -> str:
    # Converts a plain password into a secure hash
    return pwd_context.hash(password)

def verify_password(plain_password: str, hashed_password: str) -> bool:
    # Safely compares the entered password with the stored hash
    return pwd_context.verify(plain_password, hashed_password)
