# Ticket Manager API

A REST API for helpdesk ticket management built with FastAPI and SQLAlchemy. Allows managing workers and tasks — creating, assigning, updating statuses, and tracking progress.

## Tech Stack

- **Python 3.12+**
- **FastAPI** — web framework
- **SQLAlchemy** — ORM
- **SQLite** — database
- **Pydantic** — data validation
- **Uvicorn** — ASGI server

## Project Structure

```
ticket-manager/
├── main.py
└── src/
    ├── api/
    │   └── routes/
    │       ├── workers.py
    │       └── tasks.py
    ├── core/
    │   ├── back_app.py
    │   ├── config.py
    │   └── exceptions.py
    ├── db/
    │   ├── base.py
    │   ├── session.py
    │   ├── dependency.py
    │   └── queries.py
    ├── models/
    │   ├── workers.py
    │   └── tasks.py
    ├── schemas/
    │   ├── workers.py
    │   └── tasks.py
    └── services/
        ├── workers.py
        └── tasks.py
```

## Local Setup

```bash
git clone https://github.com/ndmytryshyn5/ticket-manager
cd ticket-manager
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
uvicorn main:app --reload
```

API will be available at `http://localhost:8000`  
Swagger docs at `http://localhost:8000/docs`

## Endpoints

### Workers

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/workers/` | Get all workers |
| GET | `/workers/{id}` | Get worker by ID |
| GET | `/workers/get_by_name?name=` | Get workers by name |
| POST | `/workers/add` | Add new worker |
| PATCH | `/workers/change_role/{id}` | Change worker role |
| DELETE | `/workers/{id}` | Delete worker |

### Tasks

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/tasks/` | Get all tasks |
| GET | `/tasks/{id}` | Get task by ID with assigned worker |
| POST | `/tasks/create` | Create new task |
| PATCH | `/tasks/change_status/{id}` | Change task status |
| PATCH | `/tasks/assign/{id}` | Assign worker to task |

## Data Models

### Worker
```json
{
  "id": 1,
  "worker_name": "John Doe",
  "worker_role": "Support Engineer"
}
```

### Task
```json
{
  "id": 1,
  "task_description": "Fix login issue",
  "deadline": "2024-12-31",
  "status": "open",
  "assigned_worker": "John Doe"
}
```

Task statuses: `open`, `in_progress`, `done`  
Deadline formats accepted: `dd.mm.yyyy`, `dd-mm-yyyy`, `dd/mm/yyyy`, `yyyy-mm-dd`

## License

MIT
