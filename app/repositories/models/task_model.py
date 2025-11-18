from sqlalchemy import Column, Integer, String, Boolean
from app.repositories.database import Base

class TaskModel(Base):
    __tablename__ = "task"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(255), index=True)
    completa = Column(Boolean)
    importante = Column(Boolean)
