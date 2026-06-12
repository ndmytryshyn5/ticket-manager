from sqlalchemy import create_engine, Engine
from sqlalchemy.orm import sessionmaker

from src.core.config import settings

engine: Engine = create_engine(
    settings.DATABASE_URL
)

SessionLocal: sessionmaker = sessionmaker(autocommit=False, autoflush=False, bind=engine)