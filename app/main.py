from fastapi import FastAPI
from app.routers import cats

app = FastAPI(title = "CatAlert API")
app.include_router(cats.router)

@app.get("/")
def hello():
    return "Hello world"
