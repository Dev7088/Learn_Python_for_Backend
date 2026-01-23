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

def update_user(db: Session, user_id: int, name: str, age: int):
    try:
        user = db.query(User).filter(User.id == user_id).first()

        if user is None:
            return None
        
        user.name = name
        user.age = age

        db.commit()
        db.refresh(user)
        return user
    except Exception:
        db.rollback()
        raise

def patch_user(db: Session, user_id: int, name = None, age=None):
    try:
        user = db.query(User).filter(User.id == user_id).first()
        
        if user is None:
            return None
        
        if name is not None:
            user.name = name

        if age is not None:
            user.age = age

        db.commit()
        db.refresh(user)
        return user
    
    except Exception:
        db.rollback()
        raise

def delete_user(db: Session, user_id: int):
    try:
        user = db.query(User).filter(User.id == user_id).first()

        if user is None:
            return False
        
        db.delete(user)
        db.commit()
        return True
    
    except Exception:
        db.rollback()
        raise