from sqlalchemy import Column, String, DateTime, Boolean, Integer
from sqlalchemy.sql import func
from app.database import Base

class VerificationCodeDB(Base):
    __tablename__ = "verification_codes"
    id = Column(String, primary_key=True)
    phone_number = Column(String, index=True, nullable=False)
    code = Column(String, nullable=False)
    expired_at = Column(DateTime(timezone=True), nullable=False)
    is_used = Column(Boolean, default=False)
    attempts = Column(Integer, default=0)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
