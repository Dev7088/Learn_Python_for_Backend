from pydantic import BaseModel

class UserCreate(BaseModel):
    name: str
    age: int

class UserUpdate(BaseModel):
    name: str
    age: int