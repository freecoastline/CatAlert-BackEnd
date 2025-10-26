from pydantic import BaseModel
from typing import Optional
from app.database import Base
from sqlalchemy import Column, String

class Cat(BaseModel):
    id: Optional[str] = None
    name: str
    breed: Optional[str] = None
    gender: Optional[str] = None
    birth_method: Optional[str] = None
    description: Optional[str] = None
    health_status: Optional[str] = None

class CatUpdate(BaseModel):
    name: Optional[str] = None
    breed: Optional[str] = None
    gender: Optional[str] = None
    birth_method: Optional[str] = None
    description: Optional[str] = None
    health_status: Optional[str] = None

class CatDB(Base):
    __tablename__ = "cats"

    id = Column(String, primary_key=True, index=True)
    name = Column(String, nullable=False)
    breed = Column(String, nullable=True)
    gender = Column(String, nullable=True)
    birth_method = Column(String, nullable=True)
    health_status = Column(String, nullable=True)
    description = Column(String, nullable=True)
    
