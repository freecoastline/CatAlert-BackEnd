from fastapi import HTTPException, APIRouter
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.reminder import Reminder, ReminderDB, ReminderUpdate
import uuid

router = APIRouter()


