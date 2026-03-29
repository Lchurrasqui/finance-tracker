from fastapi import FastAPI
from app.api import user
from app import models

app = FastAPI(title="Finance Tracker API")
app.include_router(user.router, prefix="/users")



@app.get("/health")
def health_check():
    return {"status": "ok"}