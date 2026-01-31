from fastapi import FastAPI
from sqlalchemy import create_engine, text
from app.config import DATABASE_URL

app = FastAPI(title="Alpha Terminal API")

engine = create_engine(DATABASE_URL, pool_pre_ping=True)

@app.on_event("startup")
def startup_db_check():
    with engine.connect() as conn:
        conn.execute(text("SELECT 1"))

@app.get("/")
def root():
    return {"status": "Backend is running"}

@app.get("/health")
def health():
    return {
        "status": "healthy",
        "database": "connected"
    }
