from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
import uuid

from app.database import get_db
from app.models.user import User, UserCreate, UserDB
from app.utils.security import hash_password, verify_password
from app.utils.jwt import create_access_token, create_refresh_token, verify_token
from app.utils.auth import get_current_user

router = APIRouter()

@router.post("/api/auth/register")
def register(user_data: UserCreate, db: Session = Depends(get_db)):
    existing_user = db.query(UserDB).filter((UserDB.username == user_data.username) | (UserDB.email == user_data.email)).first()
    if existing_user:
        raise HTTPException(status_code= status.HTTP_400_BAD_REQUEST, detail="用户名已存在")
    hashed = hash_password(user_data.password)
    new_user = UserDB(
        id=str(uuid.uuid4()),
        username=user_data.username,
        email=user_data.email,
        hashed_password=hashed,
        role="user",
        is_active=True
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return {
        "message": "注册成功",
        "user": User.model_validate(new_user)
    }

@router.post("/api/auth/login")
def login(username: str, password: str, db: Session = Depends(get_db)):
    existing_user = db.query(UserDB).filter(UserDB.username == username).first()
    if existing_user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="用户名或密码错误")
    hashed = hash_password(password)
    if not verify_password(password, hashed):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="用户名或密码错误")
    
    
    
    
    
@router.get("/api/auth/me")
def get_me(current_user: User = Depends(get_current_user)):
    return current_user

