from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from src.models.tasks import Tasks
from src.schemas.tasks import CreateTask, ChangeTaskStatus
from src.db.dependency import get_db
from src.services.tasks import TasksService

router: APIRouter = APIRouter()

@router.post("/create")
def create_task(data: CreateTask, db: Session = Depends(get_db)):
    try:
        return TasksService.create_new_task_logic(data, db)
    except Exception as e:
        raise HTTPException(status_code=400)
    
@router.patch("/change_status/{id}")
def change_task_status(id: int, data: ChangeTaskStatus, db: Session = Depends(get_db)):
    try:
        return TasksService.change_task_status(id, data, db)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))