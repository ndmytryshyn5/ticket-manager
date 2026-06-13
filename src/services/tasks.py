from sqlalchemy.orm import Session

from src.db.queries import get_worker_by_id, get_task_by_id
from src.models.tasks import Tasks

class TasksService:

    @staticmethod
    def create_new_task_logic(data, db: Session):
        task = Tasks(
            task_description = data.task_description,
            deadline = data.deadline,
            status = data.status,
            assigned_worker_id = data.worker_id
        )
    
        db.add(task)
        db.commit()
        db.refresh(task)
        return task
    
    
    @staticmethod
    def change_task_status(id: int, data, db: Session):
        task = get_task_by_id(id, db)
        if not task:
            return "Task not found"
        else:
            task.status = data.new_status

            db.commit()
            db.refresh(task)

            return{
                "status": "success",
                "message": f"Status for task.id - {task.id} changed to {data.new_status}"
            }