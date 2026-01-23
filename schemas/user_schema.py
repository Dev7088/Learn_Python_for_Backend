from pydantic import BaseModel
from typing import Optional

class UserCreate(BaseModel):
    name: str
    age: int

class UserUpdate(BaseModel):
    name: str
    age: int

class UserPatch(BaseModel):
    name: Optional[str] = None
    age: Optional[int] = None