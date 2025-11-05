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
    reminder_data = reminder.model_dump()
    reminder_data["scheduled_times"] = serialized_times
    db_reminder = ReminderDB(**reminder_data)
    db.add(db_reminder)
    db.commit()
    db.refresh(db_reminder)
    return db_reminder

@router.get("/api/reminders")
def get_reminders(db: Session = Depends(get_db)):
    reminders = db.query(ReminderDB).all()
    return reminders

@router.get("/api/reminder/{id}")
def get_reminder(id: str, db: Session = Depends(get_db)):
    reminder = db.query(ReminderDB).filter(ReminderDB.cat_id == id).first()
    if reminder is None:
        raise HTTPException(status_code=404, detail="Reminder not find")
    return reminder