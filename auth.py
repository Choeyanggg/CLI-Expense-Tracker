from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordBearer
from pwdlib import PasswordHash
from jose import jwt, JWTError
from datetime import datetime, timedelta, timezone
from models import Users
from database import get_db
from dotenv import load_dotenv
import os

load_dotenv()

password_hash=PasswordHash.recommended()

SECRET_KEY=os.getenv("SECRET_KEY")
ALGORITHM="HS256"

oauth2_scheme=OAuth2PasswordBearer(tokenUrl="login")

#hashing
def hash_password(password:str):
    return password_hash.hash(password)

def verfiy_password(plain_password:str, hashed_password:str):
    return password_hash.verify(plain_password,hashed_password)

#jwt
def create_token(data:dict):
    encode_data=data.copy()
    expire=datetime.now(timezone.utc)+timedelta(minutes=30)
    encode_data.update({
        "exp":expire
    })
    token=jwt.encode(
        encode_data,
        SECRET_KEY,
        ALGORITHM
    )
    return token

#get current user using Oauth2passwordbearer
def get_current_user(token:str=Depends(oauth2_scheme),db:Session=Depends(get_db)):
    try:
        payload=jwt.decode(token,SECRET_KEY,algorithms=[ALGORITHM])
        id=payload.get("sub")
        if id is None:
            raise HTTPException(status_code=401, detail="Invalid token")
    except JWTError:
        raise HTTPException(status_code=401, detail="Invalid token")

    user=db.query(Users).filter(Users.id==int(id)).first()
    if user is None:
        raise HTTPException(status_code=401, detail="User not found")
    return user
    