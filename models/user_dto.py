from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class UserDTO(BaseModel):
    id: int
    username: str
    email: str
    role: str
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

    class Config:
        from_attributes = True

class CreateUserDTO(BaseModel):
    username: str
    email: str
    password: str
