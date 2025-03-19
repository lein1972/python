from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from models import Base, TaskCreate, TaskRead
from services.task_service import TaskService
from typing import List

# Configuración de la base de datos MySQL
DATABASE_URL = "mysql+pymysql://root:@localhost:3306/tareas_db"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def get_task_service(db: Session = Depends(get_db)):
    return TaskService(db)

@app.post("/tareas/", response_model=TaskRead)
def create_task(task: TaskCreate, task_service: TaskService = Depends(get_task_service)):
    return task_service.create_task(task)

@app.get("/tareas/{task_id}", response_model=TaskRead)
def read_task(task_id: int, task_service: TaskService = Depends(get_task_service)):
    db_task = task_service.get_task(task_id)
    if db_task is None:
        raise HTTPException(status_code=404, detail="Tarea no encontrada")
    return db_task

@app.get("/tareas/", response_model=List[TaskRead])
def read_tasks(task_service: TaskService = Depends(get_task_service)):
    return task_service.get_tasks()

@app.put("/tareas/{task_id}", response_model=TaskRead)
def update_task(task_id: int, task: TaskCreate, task_service: TaskService = Depends(get_task_service)):
    updated_task = task_service.update_task(task_id, task.dict())
    if updated_task is None:
        raise HTTPException(status_code=404, detail="Tarea no encontrada")
    return updated_task

@app.delete("/tareas/{task_id}", status_code=204)
def delete_task(task_id: int, task_service: TaskService = Depends(get_task_service)):
    task_service.delete_task(task_id)