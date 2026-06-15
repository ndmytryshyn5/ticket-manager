from sqlalchemy.orm import Session

from src.db.queries import get_all_workers, get_worker_by_name, get_worker_by_id
from src.models.workers import Workers
from src.core.exceptions import worker_not_found

class WorkersService:

    @staticmethod
    def get_all_workers_info_logic(db: Session):
        all_workers = get_all_workers(db)

        return all_workers
    
    @staticmethod
    def add_new_worker_logic(data, db: Session):
        worker = Workers(
            worker_name=data.worker_name,
            worker_role=data.worker_role
        )

        db.add(worker)
        db.commit()
        db.refresh(worker)

        return worker

    @staticmethod
    def get_worker_by_id(id, db: Session):
        worker = get_worker_by_id(id, db)
        if not worker:
            raise worker_not_found
        
        return worker
    
    @staticmethod
    def get_worker_info_by_name(name, db: Session):
        worker = get_worker_by_name(name, db)
        if not worker:
            raise worker_not_found
        
        return worker
    
    @staticmethod
    def delete_worker_by_id(id, db: Session):
        worker = get_worker_by_id(id, db)
        if not worker:
            raise worker_not_found
        
        db.delete(worker)
        db.commit()

        return{
            "status": "deleted",
            "message": f"{worker.worker_name} deleted"
        }

    @staticmethod
    def change_worker_role(id:int, data, db: Session):
        worker = get_worker_by_id(id, db)
        if not worker:
            return "Worker not found"
        
        worker.worker_role = data.new_role

        db.commit()
        db.refresh(worker)

        return{
            "status": "success",
            "message": f"Role for {worker.worker_name} changed to {data.new_role}"
        }