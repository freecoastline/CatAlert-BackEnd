from fastapi import HTTPException, APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.reminder import Reminder, ReminderDB, ReminderUpdate, _serialize_times
import uuid
import json

router = APIRouter()

@router.post("/api/reminders")
def create_reminder(reminder: Reminder, db: Session = Depends(get_db)):
    reminder.id = str(uuid.uuid4())
    serialized_times = _serialize_times(reminder.scheduled_times)
    