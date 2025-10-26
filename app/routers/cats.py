from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.cat import CatDB
from app.models.cat import Cat, CatUpdate
import uuid

router = APIRouter()

cats_db = []

@router.post("/api/cats")
def create_cat(cat: Cat, db: Session = Depends(get_db)):
    cat.id = str(uuid.uuid4())
    db_cat = CatDB(**cat.dict())
    db.add(db_cat)
    db.commit()
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

@router.delete("/api/cats/{id}")
def delete_cat(id: str):
    for index, cat in enumerate(cats_db):
        if cat.id == id:
            del cats_db[index]
            return {"message": "Cat deleted successfully"}
    raise HTTPException(status_code=404, detail="Cat not found")


