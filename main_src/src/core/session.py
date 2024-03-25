from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from ..settings import get_settings

settings = get_settings()

SQLALCHEMY_DATABASE_URI = settings.DATABASE_URL
engine = create_engine(SQLALCHEMY_DATABASE_URI)


SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)