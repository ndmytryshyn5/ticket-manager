from pydantic import BaseModel, field_validator
from datetime import date, datetime
from typing import Optional
import re

class CreateTask(BaseModel):
    task_description: str
    deadline: date
    status: str = "open"
    worker_id: Optional[int] = None

    @field_validator("deadline", mode="before")
    @classmethod
    def parse_dedline(cls, value):
        if isinstance(value, date):
            return value
        
        normalized = re.sub(r"[.,/]", "-", str(value))

        formats = ["%d-%m-%Y", "%Y-%m-%d"]
        for fmt in formats:
            try:
                return datetime.strptime(normalized, fmt).date()
            except ValueError:
                continue

class ChangeTaskStatus(BaseModel):
    new_status: str