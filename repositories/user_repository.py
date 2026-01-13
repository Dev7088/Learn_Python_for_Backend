from sqlalchemy.orm import Session
from models.user import User

def get_all_users(db: Session):
    return db.query(User).all()

def create_user(db: Session, name: str, age: int):
    try:
        user = User(name=name, age=age)
        db.add(user)
        db.commit()
        db.refresh(user)
        return user
    except Exception:
        db.rollback()
        raise

def get_user_by_id(db: Session, user_id: int):
    return db.query(User).filter(User.id == user_id).first()