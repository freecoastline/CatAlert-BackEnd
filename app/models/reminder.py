from pydantic import BaseModel, field_validator
from typing import Optional, List
from app.database import Base
from sqlalchemy.sql import func
from sqlalchemy import Column, String, Boolean, DateTime, ForeignKey
from pydantic import ValidationError
import json
from datetime import datetime

def _serialize_times(times: List["ReminderTime"]) -> str:
    return json.dumps([time.model_dump() for time in times])
class ReminderTime(BaseModel):
    hour: int
    minute: int

def _deserialize_times(times_str: str) -> List[ReminderTime]:
    times_data = json.loads(times_str)
    return [ReminderTime(**time) for time in times_data]
class Reminder(BaseModel):
    id: Optional[str] = None
    cat_id: str
    title: str
    type: str
    frequency: str
    is_enabled: bool = True
    created_at: Optional[str] = None
    scheduled_times: List[ReminderTime]

class ReminderResponse(BaseModel):
    id: Optional[str] = None
    cat_id: str
    title: str
    type: str
    frequency: str
    is_enabled: bool = True
    created_at: Optional[datetime] = None
    scheduled_times: List[ReminderTime]
    @field_validator('scheduled_times', mode="before")
    @classmethod
    def deseraialize_times(cls, v):
        if isinstance(v, str):
            return _deserialize_times(v)
        return v
    class Config:
        from_attributes = True

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
    is_enabled = Column(Boolean, default=True)
    scheduled_times = Column(String, nullable=False)
    created_at = Column(DateTime, server_default=func.now())
    
