from fastapi import FastAPI
from app.routers import cats, reminders
from app.database import engine, Base
from app.models import cat
from app.models import reminder

app = FastAPI(title = "CatAlert API")
Base.metadata.create_all(bind=engine)
app.include_router(cats.router)
app.include_router(reminders.router)

@app.get("/")
def hello():
    return "Hello world"
