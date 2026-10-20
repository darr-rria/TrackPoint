from datetime import date
from trackpoint.models import Task

task1 = Task("Изучить SQL", "high", "todo", deadline = date(2026, 10, 20))
task2 = Task("Создать README", "medium", "in_progress")

print(task1.title)
print(task1.deadline)
print(task1.id)
print(task2.id)
