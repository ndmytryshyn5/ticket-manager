from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from src.models.workers import Workers
from src.schemas.workers import AddWorker, ChangeWorkerRole
from src.db.dependency import get_db
from src.services.workers import WorkersService

router: APIRouter = APIRouter()

@router.get("/")
def get_all_workers(db: Session = Depends(get_db)):
    try:
        return WorkersService.get_all_workers_info_logic(db)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    
@router.post("/add")
def add_worker(data: AddWorker, db: Session = Depends(get_db)):
    try:
        return WorkersService.add_new_worker_logic(data, db)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    
    
@router.get("/{id}")
def get_worker_by_id(id: int, db: Session = Depends(get_db)):
    try:
        return WorkersService.get_worker_by_id(id, db)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    
@router.get("/get_by_name")
def get_worker_by_name(name: str, db: Session = Depends(get_db)):
    try:
        return WorkersService.get_worker_info_by_name(name, db)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    
@router.delete("/{id}")
def delete_worker_by_id(id: int, db: Session = Depends(get_db)):
    try:
        return WorkersService.delete_worker_by_id(id, db)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    
@router.patch("/change_role/{id}")
def change_worker_role(id:int, data: ChangeWorkerRole, db: Session = Depends(get_db)):
    try:
        return WorkersService.change_worker_role(id, data, db)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))