from fastapi import FastAPI
from app.db.base import Base
from app.db.session import engine
from app import models  # IMPORTANT: registers all models

app = FastAPI(title="Alpha Terminal API")

@app.on_event("startup")
def startup():
    Base.metadata.create_all(bind=engine)

@app.get("/")
def root():
    return {"status": "Backend is running"}

@app.get("/health")
def health():
    return {
        "status": "healthy",
        "database": "connected"
    }
