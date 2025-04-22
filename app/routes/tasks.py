# app/routes/tasks.py

from fastapi import APIRouter

router = APIRouter(prefix="/tasks", tags=["Tasks"])

@router.get("/")
def get_tasks():
    return [{"id": 1, "title": "Tarefa de exemplo", "priority": "Alta"}]
