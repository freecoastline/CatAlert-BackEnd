from fastapi import HTTPException, APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.reminder import Reminder, ReminderDB, ReminderUpdate, _serialize_times, _deserialize_times, ReminderResponse
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
    return [
        ReminderResponse(
            **reminder.__dict__
        )
        for reminder in reminders
    ]

@router.get("/api/reminders/{id}")
def get_reminder(id: str, db: Session = Depends(get_db)):
    reminder = db.query(ReminderDB).filter(ReminderDB.id == id).first()
    if reminder is None:
        raise HTTPException(status_code=404, detail="Reminder not find")
    return reminder

@router.put("/api/reminders/{id}")
def update_reminder(id: str, reminder_update: ReminderUpdate, db: Session = Depends(get_db)):
    reminder = db.query(ReminderDB).filter(ReminderDB.id == id).first()
    if reminder is None:
        raise HTTPException(status_code=404, detail="Reminder not found")
    update_data = reminder_update.model_dump(exclude_unset=True)
    if "scheduled_times" in update_data:
        update_data["scheduled_times"] = _serialize_times(update_data["scheduled_times"])
    for key, value in update_data.items():
        setattr(reminder, key, value)
    db.commit()
    db.refresh(reminder)
    return reminder

@router.put("/api/reminders/{id}/toggle")
def toggle_reminder(id: str, db: Session = Depends(get_db)):
    reminder = db.query(ReminderDB).filter(ReminderDB.id == id).first()
    if reminder is None:
        raise HTTPException(status_code=404, detail="reminder not found")
    reminder.is_enabled = not reminder.is_enabled
    db.commit()
    db.refresh(reminder)
    return reminder

@router.delete("/api/reminders/{id}")
def delete_reminder(id: str, db: Session = Depends(get_db)):
    reminder = db.query(ReminderDB).filter(ReminderDB.id == id).first()
    if reminder is None:
        raise HTTPException(status_code=404, detail="reminder is not found")
    db.delete(reminder)
    db.commit()
    return {"message": "Reminder is deleted successfully"}