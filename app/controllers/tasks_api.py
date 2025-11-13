from fastapi import APIRouter, Depends, HTTPException
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session
from app.services.tasks_service import TaskService
from app.repositories.database import get_db
from app.schema.schemas import Task

router_api = APIRouter()
service = TaskService()

@router_api.get("/api/tasks")
def get_tasks(db: Session = Depends(get_db)):
    tasks = service.get_tasks(db)
    return JSONResponse(content=[
        {
            "id": t.id,
            "nombre": t.nombre,
            "completa": t.completa,
            "importante": t.importante
        } for t in tasks
    ])

@router_api.get("/api/tasks/{id}")
def get_task(id: int, db: Session = Depends(get_db)):
    task = service.get_task(db, id)
    if not task:
        raise HTTPException(status_code=404, detail="Tarea no encontrada")
    return JSONResponse(content={
        "id": task.id,
        "nombre": task.nombre,
        "completa": task.completa,
        "importante": task.importante
    })

@router_api.post("/api/tasks")
def create_task(task: Task, db: Session = Depends(get_db)):
    new_task = service.create_task(db, task)
    return JSONResponse(content={"message": "Tarea creada", "task_id": new_task.id})

@router_api.put("/api/tasks/{id}")
def update_task(id: int, task: Task, db: Session = Depends(get_db)):
    updated = service.update_task(db, id, task)
    return JSONResponse(content={"message": "Tarea actualizada", "task_id": updated.id})

@router_api.delete("/api/tasks/{id}")
def delete_task(id: int, db: Session = Depends(get_db)):
    deleted = service.delete_task(db, id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Tarea no encontrada")
    return JSONResponse(content={"message": "Tarea eliminada"})
