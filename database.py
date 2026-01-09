from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

DATBASE_URL = "postgresql://postgres:jashpal1972@localhost:5432/myapp_db"

engine = create_engine(DATBASE_URL)

SessionLocal = sessionmaker(bind=engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()