from sqlalchemy.orm import Session

from src.db.queries import get_worker_by_id, get_all_tasks, get_task_by_id
from src.models.tasks import Tasks
from src.core.exceptions import task_not_found, worker_not_found

class TasksService:

    @staticmethod
    def get_all_tasks_info(db: Session):
        tasks = get_all_tasks(db)

        return [
            {
                "id": task.id,
                "task_description": task.task_description,
                "deadline": task.deadline,
                "status": task.status,
                "assigned_worker_id": task.assigned_worker_id
            }
            for task in tasks
        ]
    
    @staticmethod
    def get_task_info_by_id(id: int, db: Session):
        task = get_task_by_id(id, db)
        if not task:
            raise task_not_found
        
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

        return {
            "id": task.id,
            "task_description": task.task_description,
            "deadline": task.deadline,
            "status": task.status,
            "assigned_worker_id": task.assigned_worker_id
        }
    
    
    @staticmethod
    def change_task_status(id: int, data, db: Session):
        task = get_task_by_id(id, db)
        if not task:
            raise task_not_found
        
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
            raise task_not_found
        
        if not worker:
            raise worker_not_found
        
        task.assigned_worker_id = data.worker_id

        worker.assigned_tasks += 1

        db.commit()
        db.refresh(task)
        db.refresh(worker)

        return {
            "status": "success",
            "assigned_task_id": task.id,
            "assigned_worker": worker.worker_name
        }