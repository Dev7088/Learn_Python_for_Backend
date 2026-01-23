from fastapi import FastAPI, Depends, HTTPException, status
from sqlalchemy.orm import Session
from database import get_db
from services.user_service import fetch_users, fetch_user_by_id, update_existing_user, delete_existing_user

from services.user_service import create_new_user
from schemas.user_schema import UserCreate, UserUpdate


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
    try:
        return create_new_user(db, user)
    except Exception:
        raise HTTPException(status_code=400, detail="Failed to create user")
    
@app.get("/users/{user_id}")
def get_user(user_id: int, db: Session = Depends(get_db)):
    user = fetch_user_by_id(db, user_id)

    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    
    return user

@app.put("/users/{user_id}")
def update_user_api(user_id: int, user: UserUpdate, db: Session =  Depends(get_db)):
    updated_user = update_existing_user(db, user_id, user)

    if updated_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    
    return updated_user

@app.delete("/users/{user_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_user_api(user_id: int, db: Session = Depends(get_db)):
    deleted = delete_existing_user(db, user_id)

    if not deleted:
        raise HTTPException(
            status_code=404,
            detail="User not found"
        )