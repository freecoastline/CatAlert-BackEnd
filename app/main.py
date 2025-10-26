from fastapi import FastAPI
from app.routers import cats
from app.database import engine, Base
from app.models import cat

app = FastAPI(title = "CatAlert API")
Base.metadata.create_all(bind=engine)
app.include_router(cats.router)

@app.get("/")
def hello():
    return "Hello world"
