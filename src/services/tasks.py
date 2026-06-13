from sqlalchemy.orm import Session

from src.db.queries import get_worker_by_id, get_all_tasks, get_task_by_id
from src.models.tasks import Tasks

class TasksService:

    @staticmethod
    def get_all_tasks_info(db: Session):
        all_tasks = get_all_tasks(db)

        return all_tasks
    
    @staticmethod
    def get_task_info_by_id(id: int, db: Session):
        task = get_task_by_id(id, db)
        if not task:
            return "Task not found"
        
        worker = get_worker_by_id(task.assigned_worker_id, db) if task.assigned_worker_id else None
        
        return {
            "id": task.id,
            "task_description": task.task_description,
            "deadline": task.deadline,
            "status": task.status,
            "assigned_worker": worker.worker_name if worker else None
        }


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
        
        task.status = data.new_status

        db.commit()
        db.refresh(task)

        return{
            "status": "success",
            "message": f"Status for task.id - {task.id} changed to {data.new_status}"
        }
        
    
    @staticmethod
    def assigh_worker_to_task(id: int, data, db: Session):
        task = get_task_by_id(id, db)
        worker = get_worker_by_id(data.worker_id, db)
        if not task:
            return "Task not found"
        
        if not worker:
            return "Worker not found"
        
        task.assigned_worker_id = data.worker_id

        worker.assigned_tasks += 1

        db.commit()
        db.refresh(task)
        db.refresh(worker)

        return{
            "status": "success",
            "message": f"{worker.worker_name} assigned to task {task.id}"
        }