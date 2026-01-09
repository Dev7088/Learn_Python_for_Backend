from sqlalchemy.orm import Session
from models.user import User

def get_all_users(db: Session):
    return db.query(User).all()

def create_user(db: Session, name: str, age: int):
    user = User(name=name, age=age)
    db.add(user)
    db.commit()
    db.refresh(user)
    return user