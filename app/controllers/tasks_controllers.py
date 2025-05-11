#En este archivo se crean todos los endpoints del recurso (Ejemplo: Task)
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.repositories.database import get_db
from app.services.tasks_service import TaskService
from app.schema.schemas import Task

router = APIRouter(tags=["Tareas"])

service = TaskService()

@router.get('/task')
def get_tasks(db : Session = Depends(get_db)):
    return service.get_tasks(db)

@router.get('/task/{id}')
def get_task(id : int, db : Session = Depends(get_db)):
    return service.get_task(db, id)

@router.post('/task')
def create_task(task : Task, db: Session = Depends(get_db)):
    return service.create_task(db, task)

@router.put('/task/{id}')
def update_task(id : int, task : Task, db: Session = Depends(get_db)):
    return service.update_task(db, id, task)

@router.delete('/task/{id}')
def delete_task(id : int,db : Session = Depends(get_db)):
    return service.delete_task(db, id)
