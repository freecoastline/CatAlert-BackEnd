from fastapi import FastAPI

app = FastAPI(title = "CatAlert API")

@app.get("/")
def hello():
    return "Hello world"