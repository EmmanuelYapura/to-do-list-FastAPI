#Esta capa es la que tiene todas las operaciones necesarias de las interacciones con la base de datos
from fastapi import HTTPException
from sqlalchemy.orm import Session
from app.repositories.models.task_model import TaskModel

class TaskRepository:
    def get_tasks(self, db: Session):
        return db.query(TaskModel).all()
    
    def get_task(self, db: Session, id_task : int):
        task = db.query(TaskModel).filter_by(id=id_task).first()
        if not task:
            raise HTTPException(status_code=404, detail="Tarea no encontrada")
        return task
    
    def create_task(self, db: Session, task: TaskModel):
        new_task = TaskModel(
            nombre=task.nombre,
            completa=task.completa,
            importante=task.importante
        )
        db.add(new_task)
        db.commit()
        db.refresh(new_task)
        return new_task
    
    def update_task(self, db: Session, id_task: int, task : TaskModel):
        db_task = db.query(TaskModel).filter_by(id=id_task).first()
        if not db_task:
            raise HTTPException(status_code=404, detail="La tarea no se puede modificar")
        if db_task:
            db_task.nombre = task.nombre
            db_task.completa = task.completa
            db_task.importante = task.importante
        db.commit()
        db.refresh(db_task)
        return db_task
    
    def delete_task(self, db: Session, id_task : int):
        db_task = db.query(TaskModel).filter(TaskModel.id == id_task).first()
        if db_task:
            db.delete(db_task)
            db.commit()
        return db_task
