from pydantic import BaseModel
from typing import Optional

class Cat(BaseModel):
    id: Optional[str] = None
    name: str
    breed: Optional[str] = None
    gender: Optional[str] = None
    birth_method: Optional[str] = None
    description: Optional[str] = None
    health_status: Optional[str] = None