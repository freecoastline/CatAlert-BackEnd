from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.cat import CatDB
from app.models.cat import Cat, CatUpdate
import uuid

router = APIRouter()

@router.post("/api/cats")
def create_cat(cat: Cat, db: Session = Depends(get_db)):
    cat.id = str(uuid.uuid4())
    db_cat = CatDB(**cat.dict())
    db.add(db_cat)
    db.commit()
    db.refresh(db_cat)
    return db_cat

@router.get("/api/cats")
def get_cats(db: Session = Depends(get_db)):
    cats = db.query(CatDB).all()
    return cats

@router.get("/api/cats/{id}")
def get_cat(id: str, db: Session = Depends(get_db)):
    cat = db.query(CatDB).filter(CatDB.id == id).first()
    if cat is None:
        raise HTTPException(status_code=404, detail= "Cat not found")       
    return cat
    
@router.put("/api/cats/{id}")
def update_cat(id: str, cat_update: CatUpdate, db: Session = Depends(get_db)):
    cat = db.query(CatDB).filter(CatDB.id == id).first()
    if cat is None:
        raise HTTPException(status_code=404, detail="Cat not found")
    
    update_data = cat_update.dict(exclude_unset=True)

    for key, value in update_data.items():
        setattr(cat, key, value)

    db.commit()
    db.refresh(cat)
    return cat

@router.delete("/api/cats/{id}")
def delete_cat(id: str, db: Session = Depends(get_db)):
    cat = db.query(CatDB).filter(CatDB.id == id).first()
    if cat is None:
        raise HTTPException(status_code=404, detail="Cat not found")
    db.delete(cat)
    db.commit()
    
    return {"message": "Cat deleted successfully"}


