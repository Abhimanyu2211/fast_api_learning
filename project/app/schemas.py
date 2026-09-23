from pydantic import BaseModel, EmailStr, Field

class UserCreate(BaseModel):
    # Field helps us add extra validation like min_length
    username: str = Field(..., min_length=3, description="Username must be at least 3 characters")
    email: EmailStr
    password: str = Field(..., min_length=6, description="Password must be at least 6 characters")

# We use this schema to validate login requests
class UserLogin(BaseModel):
    username: str
    password: str
