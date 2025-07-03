#En este archivo se crean todos los endpoints del recurso (Ejemplo: Task)
from fastapi import APIRouter, Depends, Request
from sqlalchemy.orm import Session

from app.repositories.database import get_db
from app.services.tasks_service import TaskService
from app.schema.schemas import Task

from fastapi.templating import Jinja2Templates

router = APIRouter(tags=["Tareas"])

service = TaskService()

templates = Jinja2Templates(directory="app/templates")


@router.get('/task')
def get_tasks(request: Request, db : Session = Depends(get_db)):
    tasks = service.get_tasks(db)
    return templates.TemplateResponse("home.html", {"request": request, "tasks" : tasks})

@router.get('/task/{id}')
def get_task(id : int, request: Request, db : Session = Depends(get_db)):
    return templates.TemplateResponse("home.html",{"request": request, "tasks": [service.get_task(db, id)]})

@router.post('/task')
def create_task(task : Task, db: Session = Depends(get_db)):
    return service.create_task(db, task)

@router.put('/task/{id}')
def update_task(id : int, task : Task, db: Session = Depends(get_db)):
    return service.update_task(db, id, task)

@router.delete('/task/{id}')
def delete_task(id : int,db : Session = Depends(get_db)):
    return service.delete_task(db, id)
