from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import relationship

from src.db.base import Base

class Tasks(Base):
    __tablename__ = 'tasks'

    id: Column = Column(Integer, primary_key=True)
    task_description: Column = Column(String, nullable=False)
    deadline: Column = Column(Date, nullable=False)
    status: Column = Column(String, nullable=False, default="open")
    assigned_worker_id: Column = Column(Integer, ForeignKey('workers.id'), nullable=True)

    worker = relationship("Worker", back_populates="tasks")