from pydantic import BaseModel
from app.database import Base
from typing import Optional
from sqlalchemy import Column, String, DateTime, ForeignKey
from sqlalchemy.sql import func

class UserCreate(BaseModel):
    id: str
    username: Optional[str] = None
    email: str

class UserDB(Base):
    id: str
    username: Optional[str] = None
    email: str
    hashed_password: str
    rold: str
    is_active: bool
    created_at: str
    