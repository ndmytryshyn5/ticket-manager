from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from src.models.tasks import Tasks

router: APIRouter = APIRouter()