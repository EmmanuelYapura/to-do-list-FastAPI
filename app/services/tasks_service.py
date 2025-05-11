# En esta capa se maneja logica de negocios, un ejemplo a modificar puede ser la validacion de usuarios(admin para retornar algo)
from sqlalchemy.orm import Session
from app.repositories.tasks_repository import TaskRepository
from app.repositories.models.task_model import TaskModel

class TaskService:
    def __init__(self):
        self.repository : TaskRepository = TaskRepository()

    def get_tasks(self, db: Session):
        return self.repository.get_tasks(db)
    
    def get_task(self,db: Session, id_task : int):
        return self.repository.get_task(db,id_task)
    
    def create_task(self, db: Session, task: TaskModel):
        return self.repository.create_task(db,task)
    
    def update_task(self, db: Session, id_task : int , task: TaskModel):
        return self.repository.update_task(db,id_task, task)
    
    def delete_task(self,db: Session, id_task : int):
        return self.repository.delete_task(db,id_task)
    