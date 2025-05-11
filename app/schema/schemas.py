# Esta capa es para los esquemas que voy a utilizar como base model
from pydantic import BaseModel

class Task(BaseModel):
    nombre: str
    completa: bool
    importante: bool
