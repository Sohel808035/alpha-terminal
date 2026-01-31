from fastapi import FastAPI

app = FastAPI(title="Alpha Terminal API")

@app.get("/")
def root():
    return {"status": "Backend is running"}

@app.get("/health")
def health():
    return {
        "status": "healthy",
        "version": "1.0.0",
        "environment": "development"
    }
