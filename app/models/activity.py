from pydantic import BaseModel
from app.database import Base
from typing import Optional
from sqlalchemy import Column, String, DateTime, ForeignKey
from sqlalchemy.sql import func
from datetime import datetime


class Activity(BaseModel):
    id: str 
    reminder_id: str
    cat_id: str
    type: str
    schedule_time: datetime
    complete_time: Optional[datetime] = None
    status: str 


class ActivityDB(Base):
    __tablename__ = "activities"
    id = Column(String, primary_key=True)
    reminder_id = Column(String, index=True, nullable=False)
    cat_id = Column(String, index=True, nullable=False)
    type = Column(String, nullable=False)
    schedule_time = Column(DateTime(timezone=True), nullable=False)
    complete_time = Column(DateTime(timezone=True), nullable=True)
    status = Column(String, nullable=False)