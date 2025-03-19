from sqlalchemy.orm import Session
from repositories import task_repository
from models import TaskCreate

class TaskService:
    def __init__(self, db: Session):
        self.db = db

    def get_tasks(self):
        return task_repository.get_tasks(self.db)

    def get_task(self, task_id: int):
        return task_repository.get_task(self.db, task_id)

    def create_task(self, task: TaskCreate):
        return task_repository.create_task(self.db, task)

    def update_task(self, task_id: int, task_data: dict):
        return task_repository.update_task(self.db, task_id, task_data)

    def delete_task(self, task_id: int):
        return task_repository.delete_task(self.db, task_id)