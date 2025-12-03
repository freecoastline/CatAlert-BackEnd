from fastapi import FastAPI
from app.routers import cats, reminders, auth, activity
from app.database import engine, Base
from app.models import cat
from app.models import reminder
from app.models import user

app = FastAPI(title = "CatAlert API")
Base.metadata.create_all(bind=engine)
app.include_router(cats.router)
app.include_router(reminders.router)
app.include_router(auth.router)
app.include_router(activity.router)

@app.get("/")
def hello():
    return "Hello world"
