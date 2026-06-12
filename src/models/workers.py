from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from src.db.base import Base

class Workers(Base):
    __tablename__ = 'workers'

    id: Column = Column(Integer, primary_key=True)
    worker_name: Column = Column(String, nullable=False)
    role: Column = Column(String, nullable=False)

    tasks = relationship("Task", back_populates="worker")