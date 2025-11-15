from pydantic import BaseModel
from app.database import Base
from typing import Optional
from sqlalchemy import Column, String, DateTime, ForeignKey
from sqlalchemy.sql import func

class UserCreate(BaseModel):
    password: str
    username: Optional[str] = None
    email: str

class UserDB(Base):
    __tablename__ = "users"
    id =  Column(String, primary_key=True, index=True)
    username = Column(String, unique=True, index=True, nullable=False)
    email = Column(String,nullable=False )
    hashed_password = Column(String, nullable=False)
    role = Column(String, default="user")
    is_active = Column(bool, default=True)
    created_at = Column(DateTime, nullable=False)
    