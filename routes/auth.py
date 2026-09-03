from fastapi import APIRouter,Depends,HTTPException
from sqlalchemy.orm import Session
from database import get_db
from schemas import TokenResponse,LoginRequest
from models import Users
from auth import create_token, verfiy_password

router=APIRouter()

@router.post("/login", response_model=TokenResponse)
def login(users:LoginRequest,db:Session=Depends(get_db)):
    existing_user=db.query(Users).filter(Users.username==users.username).first()
    if not existing_user or not verfiy_password(users.password,existing_user.password_hash):
        raise HTTPException(status_code=401, detail="User invalid or password")
    token=create_token({
        "sub":str(existing_user.id)
    })
    return {
        "access_token": token,
        "token_type": "bearer"
    }