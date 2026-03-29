from sqlalchemy import select
from app.schemas.user import UserCreate
from sqlalchemy.orm import Session
from app.models.user import User
from passlib.hash import bcrypt

class UserAlreadyExistsException(Exception):
    pass

def check_email_not_taken(email: str, db: Session):
    # Logic to check if the email already exists in the database
    exists = bool(db.execute(select(User).where(User.email == email)).first())
    if exists:
        raise UserAlreadyExistsException(f"Email {email} is already taken.")

def create_user(user: UserCreate, db: Session) -> User:
    # Logic to create a new user in the database
    email = user.email
    
    check_email_not_taken(email, db)
    
    password = bcrypt.hash(user.password)
    
    new_user = User(email=email, password_hash=password)
    
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    
    return new_user