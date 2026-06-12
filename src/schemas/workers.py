from pydantic import BaseModel

class AddWorker(BaseModel):
    worker_name: str
    worker_role: str