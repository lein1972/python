from sqlalchemy import create_engine, Column, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base
from pydantic import BaseModel

Base = declarative_base()

class Task(Base):
    __tablename__ = "tareas"
    id = Column(Integer, primary_key=True, index=True)
    titulo = Column(String)
    descripcion = Column(String)
    completado = Column(Boolean, default=False)

class TaskBase(BaseModel):
    titulo: str
    descripcion: str
    completado: bool

class TaskCreate(TaskBase):
    pass

class TaskRead(TaskBase):
    id: int