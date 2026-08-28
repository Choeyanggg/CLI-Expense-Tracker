from fastapi import APIRouter,Depends,HTTPException
from sqlalchemy.orm import Session

from models import Users
from schemas import UserCreate,UserResponse
from database import get_db
from auth import hash_password

router=APIRouter()

@router.post("/register", response_model=UserResponse)
def create_user(user:UserCreate, db:Session=Depends(get_db)):
    existing_user=db.query(Users).filter(Users.username==user.username).first()
    if existing_user:
        raise HTTPException(status_code=400, detail="Username already exitst")
    hashed_password=hash_password(user.password)
    newuser=Users(username=user.username, password_hash=hashed_password)
    db.add(newuser)
    db.commit()
    db.refresh(newuser)
    return newuser