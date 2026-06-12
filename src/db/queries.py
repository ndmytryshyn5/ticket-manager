from sqlalchemy.orm import Session
from sqlalchemy import exists, select

from src.models.workers import Workers
from src.models.tasks import Tasks

def get_all_workers(db: Session):
    return db.execute(select(Workers)).scalars().all()