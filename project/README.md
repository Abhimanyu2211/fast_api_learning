# FastAPI MySQL Login System

## Technologies
* Python
* FastAPI
* MySQL
* SQLAlchemy
* Pydantic
* Jinja2
* HTML/CSS

## Features
* User registration
* Login
* Password hashing
* MySQL database
* Input validation
* Error handling
* Database session management

## Setup

1. **Clone or create directory**
```bash
mkdir fastapi_login
cd fastapi_login
```

2. **Virtual Environment**
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Database Setup

```sql
CREATE DATABASE login_db;
CREATE USER 'fastapi_user'@'localhost' IDENTIFIED BY 'strong_password';
GRANT ALL PRIVILEGES ON login_db.* TO 'fastapi_user'@'localhost';
FLUSH PRIVILEGES;

USE login_db;
CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) NOT NULL UNIQUE,
    email VARCHAR(100) NOT NULL UNIQUE,
    password_hash VARCHAR(255) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

## Running the application
```bash
uvicorn app.main:app --reload
```
Open `http://127.0.0.1:8000` in your browser.

## Testing
- Register a user with valid details.
- Try registering a duplicate user or email.
- Login with the created user.
- Enter wrong credentials to see the generic error message.
