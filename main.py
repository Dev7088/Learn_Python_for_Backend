from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from database import get_db
from services.user_service import fetch_users

from services.user_service import create_new_user
from schemas.user_schema import UserCreate
# from pydantic import BaseModel

app = FastAPI()

# class User(BaseModel):
#     name : str
#     age : int


@app.get("/")
def root():
    print("Hello Dev")
    return { "message" : "Hello Dev" }

# @app.get("/hello")
# def hello(name: str):
#     return { "message": f"Hello {name}"}

@app.get("/users")
def get_users(db: Session = Depends(get_db)):
    return fetch_users(db)

@app.post("/users")
def create_user_api(user: UserCreate, db: Session = Depends(get_db)):
    return create_new_user(db, user)