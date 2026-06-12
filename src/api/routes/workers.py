from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from src.models.workers import Workers
from src.schemas.workers import AddWorker
from src.db.dependency import get_db
from src.services.workers import WorkersService

router: APIRouter = APIRouter()

@router.post("/add")
def add_worker(data: AddWorker, db: Session = Depends(get_db)):
    try:
        return WorkersService.add_new_worker_logic(data, db)
    except Exception as e:
        print(f"Error occurred: {e}")
        raise HTTPException(status_code=400)