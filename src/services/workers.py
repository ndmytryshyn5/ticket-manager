from sqlalchemy.orm import Session

from src.db.queries import get_all_workers
from src.models.workers import Workers

class WorkersService:

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



    # @staticmethod
    # def get_workers_info_logic(worker: Workers, db: Session):
    #     all_workers = get_all_workers(worker,)