# Esta capa es para los esquemas que voy a utilizar como base model
from pydantic import BaseModel
from typing import Optional

class Task(BaseModel):
    nombre: str
    completa: bool
    importante: bool

class TaskUpdate(BaseModel):
    nombre: Optional[str] = None
    completa: Optional[bool] = None
    importante: Optional[bool] = None

class TaskResponse(Task):
    id: int

    class Config:
        from_attributes = True