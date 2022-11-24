import uvicorn
from fastapi import FastAPI
from router import event
from db import models
from db.database import engine

app = FastAPI()

@app.get("/")
def root():
    return {"title": "Hello World"}

app.include_router(event.router)

models.Base.metadata.create_all(engine)

if __name__ == "__main__":
    uvicorn.run("app:app", host="0.0.0.0", port=8000, reload=True)
