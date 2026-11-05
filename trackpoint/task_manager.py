#управляет задачами: добавляет, ищет, изменяет

from .models import Task

class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, task: Task):
        self.tasks.append(task)

    def get_all_tasks(self):
        return self.tasks

    def get_task_by_id(self, task_id: int):
        for task in self.tasks:
            if task.id == task_id:
                return task
        return None