from sqlalchemy.orm import Session

from src.db.queries import get_all_workers, get_worker_by_name, get_worker_by_id
from src.models.workers import Workers
from src.core.exceptions import worker_not_found

class WorkersService:

    @staticmethod
    def get_all_workers_info_logic(db: Session):
        workers = get_all_workers(db)

        return [
            {
                "id": worker.id,
                "worker_name": worker.worker_name,
                "worker_role": worker.worker_role
            }
            for worker in workers
        ]
    
    @staticmethod
    def add_new_worker_logic(data, db: Session):
        worker = Workers(
            worker_name=data.worker_name,
            worker_role=data.worker_role
        )

        db.add(worker)
        db.commit()
        db.refresh(worker)

        return {
            "id": worker.id,
            "worker_name": worker.worker_name,
            "worker_role": worker.worker_role
        }

    @staticmethod
    def get_worker_by_id(id, db: Session):
        worker = get_worker_by_id(id, db)
        if not worker:
            raise worker_not_found
        
        return {
            "id": worker.id,
            "worker_name": worker.worker_name,
            "worker_role": worker.worker_role
        }
    
    @staticmethod
    def get_worker_info_by_name(name, db: Session):
        workers = get_worker_by_name(name, db)
        if not workers:
            raise worker_not_found
        
        return [
        {
            "id": worker.id,
            "worker_name": worker.worker_name,
            "worker_role": worker.worker_role
        }
        for worker in workers
    ]
    
    @staticmethod
    def delete_worker_by_id(id, db: Session):
        worker = get_worker_by_id(id, db)
        if not worker:
            raise worker_not_found
        
        db.delete(worker)
        db.commit()

        return {
            "status": "deleted",
            "deleted_worker": worker.worker_name
        }

    @staticmethod
    def change_worker_role(id:int, data, db: Session):
        worker = get_worker_by_id(id, db)
        if not worker:
            return "Worker not found"
        
        worker.worker_role = data.new_role

        db.commit()
        db.refresh(worker)

        return {
            "status": "success",
            "worker": worker.worker_name,
            "new_role": worker.worker_role
        }