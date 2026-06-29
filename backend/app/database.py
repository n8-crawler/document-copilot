from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker,declarative_base
from app.config import settings

engine = create_engine(settings.DATABASE_URL)
sessionlocal = sessionmaker(autoflush=False,autocommit=False,bind=engine)
base = declarative_base()

def get_db():
    db = sessionlocal()
    try:
        yield db
    finally:
        db.close()