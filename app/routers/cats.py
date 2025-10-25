from fastapi import APIRouter
from fastapi import HTTPException
from app.models.cat import Cat
import uuid

router = APIRouter()

cats_db = []

@router.post("/api/cats")
def create_cat(cat: Cat):
    cat.id = str(uuid.uuid4())
    cats_db.append(cat)
    return cat

@router.get("/api/cats")
def get_cats():
    return cats_db

@router.get("/api/cats/{id}")
def get_cat(id: str):
    for cat in cats_db:
        if cat.id == id:
            return cat
    return HTTPException(status_code=404, detail= "Cat not found")
