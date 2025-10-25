from fastapi import APIRouter, HTTPException
from app.models.cat import Cat, CatUpdate
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
    raise HTTPException(status_code=404, detail= "Cat not found")

@router.put("/api/cats/{id}")
def update_cat(id: str, cat_update: CatUpdate):
    for cat in cats_db:
        if cat.id == id:
            update_data = cat_update.dict(exclude_unset=True)

            for key, value in update_data.items():
                setattr(cat, key, value)
            return cat
    raise HTTPException(status_code=404, detail="Cat not found")
