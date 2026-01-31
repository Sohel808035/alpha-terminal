from fastapi import FastAPI
from app.db.base import Base
from app.db.session import engine
from app import models
from app.routes.users import router as users_router

app = FastAPI(title="Alpha Terminal API")

@app.on_event("startup")
def startup():
    Base.metadata.create_all(bind=engine)

app.include_router(users_router)

@app.get("/")
def root():
    return {"status": "Backend is running"}

@app.get("/health")
def health():
    return {
        "status": "healthy",
        "database": "connected"
    }
