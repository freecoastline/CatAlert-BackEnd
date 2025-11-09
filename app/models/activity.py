from pydantic import BaseModel
from app.database import Base
from typing import Optional
from sqlalchemy import Column, String, DateTime, ForeignKey
from sqlalchemy.sql import func


class Activity(BaseModel):
    id: Optional[str] = None
    cat_id: str
    type: str
    title: str
    description: Optional[str] = None
    timestamp: str
    created_at: Optional[str] = None

