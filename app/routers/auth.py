from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
import uuid

from app.database import get_db
from app.models.user import User, UserCreate, UserDB
from app.utils.security import hash_password, verify_password
from app.utils.jwt import create_access_token, create_refresh_token, verify_token
from app.utils.auth import get_current_user

router = APIRouter()

@router.get("api/auth/me")
def get_me(current_user: User = Depends(get_current_user)):
    return current_user

