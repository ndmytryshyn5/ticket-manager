from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from src.models.workers import Workers

router: APIRouter = APIRouter()