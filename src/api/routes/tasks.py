from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from src.models.tasks import Tasks
from src.schemas.tasks import CreateTask, ChangeTaskStatus, AssignWorker
from src.db.dependency import get_db
from src.services.tasks import TasksService
from src.core.exceptions import bad_request

router: APIRouter = APIRouter()

@router.get("/")
def get_all_tasks(db: Session = Depends(get_db)):
    try:
        return TasksService.get_all_tasks_info(db)
    except Exception as e:
        raise bad_request(str(e))
    
@router.post("/create")
def create_task(data: CreateTask, db: Session = Depends(get_db)):
    try:
        return TasksService.create_new_task_logic(data, db)
    except Exception as e:
        raise bad_request(str(e))
    
@router.patch("/change_status/{id}")
def change_task_status(id: int, data: ChangeTaskStatus, db: Session = Depends(get_db)):
    try:
        return TasksService.change_task_status(id, data, db)
    except Exception as e:
        raise bad_request(str(e))
    
@router.get("/{id}")
def get_task_by_id(id: int, db: Session = Depends(get_db)):
    try:
        return TasksService.get_task_info_by_id(id, db)
    except Exception as e:
        raise bad_request(str(e))


@router.patch("/assign/{id}")
def assign_worker_to_task(id:int, data: AssignWorker, db: Session = Depends(get_db)):
    try:
        return TasksService.assigh_worker_to_task(id, data, db)
    except Exception as e:
        raise bad_request(str(e))