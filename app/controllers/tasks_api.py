from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.services.tasks_service import TaskService
from app.repositories.database import get_db
from app.schema.schemas import TaskResponse, Task, TaskUpdate

router_api = APIRouter()
service = TaskService()

@router_api.get("/api/tasks", response_model=list[TaskResponse])
def get_tasks(db: Session = Depends(get_db)):
    tasks = service.get_tasks(db)
    return tasks

@router_api.get("/api/tasks/{id}", response_model=TaskResponse)
def get_task(id: int, db: Session = Depends(get_db)):
    task = service.get_task(db, id)
    if not task:
        raise HTTPException(status_code=404, detail="Tarea no encontrada")
    return task

@router_api.post("/api/tasks", response_model=TaskResponse)
def create_task(task: Task, db: Session = Depends(get_db)):
    new_task = service.create_task(db, task)
    return new_task

@router_api.put("/api/tasks/{id}", response_model=TaskResponse)
def update_task(id: int, task: TaskUpdate, db: Session = Depends(get_db)):
    updated = service.update_task(db, id, task)
    return updated

@router_api.delete("/api/tasks/{id}")
def delete_task(id: int, db: Session = Depends(get_db)):
    deleted = service.delete_task(db, id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Tarea no encontrada")
    return  {"message": "Tarea eliminada"}
