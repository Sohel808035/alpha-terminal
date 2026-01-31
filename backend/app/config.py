import os

DATABASE_URL = (
    f"postgresql://{os.getenv('POSTGRES_USER')}:"
    f"{os.getenv('POSTGRES_PASSWORD')}@"
    f"postgres:5432/"
    f"{os.getenv('POSTGRES_DB')}"
)
