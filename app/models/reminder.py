from pydantic import BaseModel
from typing import Optional, List
from app.database import Base
from sqlalchemy.sql import func
from sqlalchemy import Column, String, Boolean, DateTime, ForeignKey

class ReminderTime(BaseModel):
    hour: int
    minute: int

class Reminder(BaseModel):
    id: Optional[str] = None
    cat_id: str
    title: str
    type: str
    frequency: str
    is_enabled: bool = True
    created_at: Optional[str] = None
    scheduled_times: List[ReminderTime]

class ReminderUpdate(BaseModel):
    title: Optional[str] = None
    type: Optional[str] = None
    frequency: Optional[str] = None
    is_enabled: Optional[bool] = None
    scheduled_times: Optional[List[ReminderTime]] = None

class ReminderDB(Base):
    __tablename__ = "reminders"
    id = Column(String, primary_key=True, index=True)
    cat_id = Column(String, ForeignKey("cats.id"), nullable=False, index=True)
    title = Column(String, nullable=False)
    type = Column(String, nullable=False)
    frequency = Column(String, nullable=False)
    is_enabled = Column(Boolean, nullable=False)
    scheduled_times = Column(String, nullable=False)
    created_at = Column(DateTime, server_default=func.now())
    