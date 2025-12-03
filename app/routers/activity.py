from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
import uuid

from app.database import get_db
from app.models.activity import Activity, ActivityDB, ActivityResponse, ActivityUpdate
from app.utils.security import hash_password, verify_password
from app.utils.jwt import create_access_token, create_refresh_token, verify_token
from app.utils.auth import get_current_user
from jose import JWTError

router = APIRouter()


@router.get("/api/activity")
def get_activities(db: Session = Depends(get_db)):
    activities = db.query(ActivityDB).all()
    return [
        ActivityResponse.model_validate(activity)
        for activity in activities
    ]

@router.get("/api/activity/{id}")
def get_activity(id: str, db: Session = Depends(get_db)):
    activity = db.query(ActivityDB).filter(ActivityDB.id == id).first()
    if activity is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="activity　not found!")
