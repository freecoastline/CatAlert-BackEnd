from pydantic import BaseModel, EmailStr
from app.database import Base
from typing import Optional
from sqlalchemy import Column, String, DateTime, ForeignKey, Boolean
from sqlalchemy.sql import func
from datetime import datetime

class UserCreate(BaseModel):
    password: str
    username: str
    email: EmailStr

class User(BaseModel):
    id: str
    username: str
    email: str
    role: str
    is_active: bool
    created_at: datetime
    class Config: 
        from_attributes = True

class UserDB(Base):
    __tablename__ = "users"
    id =  Column(String, primary_key=True, index=True)
    username = Column(String, unique=True,index=True, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    role = Column(String, default="user", nullable=False)
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

    