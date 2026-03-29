from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas.user import UserCreate, UserResponse
from app.core.database import SessionLocal
from app.services.user_service import UserAlreadyExistsException, create_user as create_user_service

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=UserResponse, status_code=201)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    try:
        new_user = create_user_service(user, db)
    except UserAlreadyExistsException as e:
        raise HTTPException(status_code=400, detail=str(e))
    return new_user