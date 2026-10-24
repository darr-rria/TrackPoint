from datetime import date
from trackpoint.models import Task
from trackpoint.task_manager import TaskManager

task_manager = TaskManager()
task1 = Task("Изучить SQL", "high", "todo", deadline = date(2026, 10, 20))
task2 = Task("Создать README", "medium", "in_progress")

task_manager.add_task(task1)
task_manager.add_task(task2)

print("Список задач:")
for task in task_manager.get_all_tasks():
    print(f"- {task.title}")