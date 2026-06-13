from sqlalchemy.orm import Session
from sqlalchemy import exists, select

from src.models.workers import Workers
from src.models.tasks import Tasks

def get_all_workers(db: Session):
    return db.execute(select(Workers)).scalars().all()

def get_worker_by_id(id: int, db: Session):
    return db.query(Workers).filter(Workers.id == id).first()

def get_worker_by_name(name: str, db: Session):
    return db.query(Workers).filter(Workers.worker_name == name).all()

def get_task_by_id(id: int, db: Session):
    return db.query(Tasks).filter(Tasks.id == id).first()