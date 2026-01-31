from pydantic import BaseModel, EmailStr
import uuid

class UserCreate(BaseModel):
    email: EmailStr
    full_name: str

class UserRead(BaseModel):
    id: uuid.UUID
    email: EmailStr
    full_name: str

    class Config:
        from_attributes = True
