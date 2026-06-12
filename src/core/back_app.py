from fastapi import FastAPI

from src.core.config import settings
from src.db.base import Base
from src.db.session import engine

from src.api.routes import workers as workers_routes
from src.api.routes import tasks as tasks_routes

class BackendApp(FastAPI):
    def __init__(self):
        super().__init__()
        self.__initializeRoutes()
        
        Base.metadata.create_all(bind=engine)

    def __initializeRoutes(self):
        self.include_router(workers_routes.router, prefix="/workers", tags=["workers"])
        self.include_router(tasks_routes.router, prefix="/tasks", tags=["tasks"])

        @self.get("/")
        def read_root():
            return {"Status": "Server up and running"}