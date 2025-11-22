from pydantic import BaseModel, EmailStr, field_serializer
from app.database import Base
from typing import Optional
from sqlalchemy import Column, String, DateTime, ForeignKey, Boolean
from sqlalchemy.sql import func
from datetime import datetime,timezone

class UserCreate(BaseModel):
    password: str
    username: str
    email: EmailStr
    phone_number: str

class User(BaseModel):
    id: str
    username: str
    email: str
    role: str
    is_active: bool
    phone_number: Optional[str] = None
    phone_verified: bool = False
    created_at: datetime
    @field_serializer('created_at')
    def serialize_dt(self, dt: datetime):
        if dt and dt.tzinfo is None:
            dt = dt.replace(tzinfo=timezone.utc)
        return dt.isoformat() if dt else None
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
    phone_number = Column(String, nullable=False, unique=True)
    phone_verified = Column(Boolean, default=False)

    