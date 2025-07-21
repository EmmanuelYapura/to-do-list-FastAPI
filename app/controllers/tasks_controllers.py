#En este archivo se crean todos los endpoints del recurso (Ejemplo: Task)
from fastapi import APIRouter, Depends, Request, Form, HTTPException
from fastapi.responses import RedirectResponse
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
def create_task(nombre: str = Form(...), completa: bool = Form(False), importante : bool = Form(False), db: Session = Depends(get_db)):
    task = Task(nombre=nombre, completa=completa, importante=importante)
    service.create_task(db, task)
    return RedirectResponse(url='/task' , status_code=303) 

@router.get('/edit_task/{id}')
def get_edit_task_form(request: Request, id: int, db: Session = Depends(get_db)):
    task = service.get_task(db, id)
    if not task:
        raise HTTPException(status_code=404, detail="Tarea no encontrada para editar")
    return templates.TemplateResponse("edit_task.html", {"request": request, "task": task})

@router.post('/task/{id}/update')
def update_task_from_form(
    id: int,
    nombre: str = Form(...),
    completa: bool = Form(False),
    importante: bool = Form(False),
    db: Session = Depends(get_db)
):
    updated_data = Task(id=id, nombre=nombre, completa=completa, importante=importante)

    updated_task = service.update_task(db, id, updated_data)
    if not updated_task:
        raise HTTPException(status_code=404, detail="Tarea no encontrada para actualizar")
    return RedirectResponse(url='/task', status_code=303) 

@router.post('/task/{id}/delete')
def delete_task_from_form(id: int, db: Session = Depends(get_db)):
    deleted_task = service.delete_task(db, id)
    if not deleted_task:
        raise HTTPException(status_code=404, detail="Tarea no encontrada para eliminar")
    return RedirectResponse(url='/task', status_code=303) 
