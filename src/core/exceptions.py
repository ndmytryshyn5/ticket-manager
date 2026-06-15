from fastapi import HTTPException, status

def bad_request(reason: str = "Bad Request") -> HTTPException:
    return HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=reason)

def internal_server_error(reason: str = "Internal Server Error") -> HTTPException:
    return HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=reason)

worker_not_found: HTTPException = HTTPException(
    status_code=status.HTTP_404_NOT_FOUND,
    detail="Worker not found"
)

worker_already_exists: HTTPException = HTTPException(
    status_code=status.HTTP_409_CONFLICT,
    detail="Worker already exists"
)


task_not_found: HTTPException = HTTPException(
    status_code=status.HTTP_404_NOT_FOUND,
    detail="Task not found"
)

invalid_status: HTTPException = HTTPException(
    status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
    detail="Invalid status value"
)