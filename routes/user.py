from fastapi import APIRouter,Depends,HTTPException
from sqlalchemy.orm import Session

from ..models import Users
from ..schemas import UserCreate,UserResponse
from ..database import get_db
from ..auth import hash_password

route=APIRouter()

@route.post("/register", response_model=UserResponse)
def create_user(user:UserCreate, db:Session=Depends(get_db)):
    existing_user=db.query(Users).filter(Users.username==user.username).first()
    if existing_user:
        raise HTTPException(status_code=400, detail="Username already exitst")
    password_hash=hash_password(user.password)
    newuser=Users(username=user.username, password=password_hash)
    db.add(newuser)
    db.commit()
    db.refresh(newuser)
    return newuser