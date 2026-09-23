from fastapi import FastAPI, Depends, Form, Request, HTTPException, status
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from sqlalchemy.orm import Session
from . import models, schemas, crud, auth
from .database import engine, get_db

# Create all database tables (if they don't exist)
models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="FastAPI Login System")

# Serve static files (like CSS)
app.mount("/static", StaticFiles(directory="static"), name="static")

# Set up templates directory
templates = Jinja2Templates(directory="app/templates")

@app.get("/", response_class=HTMLResponse)
def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/register", response_class=HTMLResponse)
def get_register_page(request: Request):
    return templates.TemplateResponse("register.html", {"request": request})

@app.get("/login", response_class=HTMLResponse)
def get_login_page(request: Request):
    return templates.TemplateResponse("login.html", {"request": request})

@app.post("/register")
def register_user(
    request: Request,
    username: str = Form(...),
    email: str = Form(...),
    password: str = Form(...),
    db: Session = Depends(get_db)
):
    # Create Pydantic schema to validate data automatically
    try:
        user_data = schemas.UserCreate(username=username, email=email, password=password)
    except Exception as e:
        # If Pydantic validation fails (e.g., bad email), show an error
        return templates.TemplateResponse("register.html", {"request": request, "error": "Invalid form data (Ensure valid email & min 6 char password)"})

    # Check if username exists
    if crud.get_user_by_username(db, username=user_data.username):
        return templates.TemplateResponse("register.html", {"request": request, "error": "Username already exists"})
    
    # Check if email exists
    if crud.get_user_by_email(db, email=user_data.email):
        return templates.TemplateResponse("register.html", {"request": request, "error": "Email already exists"})
    
    # Create user
    try:
        crud.create_user(db=db, user=user_data)
        return templates.TemplateResponse("login.html", {"request": request, "success": "Registration successful! Please login."})
    except Exception as e:
        return templates.TemplateResponse("register.html", {"request": request, "error": "Database error occurred"})

@app.post("/login")
def login_user(
    request: Request,
    username: str = Form(...),
    password: str = Form(...),
    db: Session = Depends(get_db)
):
    # Find user in MySQL
    user = crud.get_user_by_username(db, username=username)
    
    # Verify password hash. 
    # Use generic message for both wrong username OR wrong password
    if not user or not auth.verify_password(password, user.password_hash):
        return templates.TemplateResponse("login.html", {"request": request, "error": "Invalid username or password"})
    
    # Correct login
    return templates.TemplateResponse("success.html", {"request": request, "username": user.username})
