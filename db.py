#db.py
from sqlalchemy import create_engine 
from sqlalchemy.orm import sessionmaker, declarative_base

# ✅ Correct URL format
SQLALCHEMY_DATABASE_URL = "postgresql://postgres:YourNewPassword@localhost:5432/bookstore"


# ✅ Typo fix: 'engin' → 'engine'
engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# ✅ This is fine, but make sure models are imported before calling
def create_table():
    Base.metadata.create_all(bind=engine)
