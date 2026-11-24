# описывает, что такое задача

from datetime import date
from itertools import count

_id_counter = count(1)  # счетчик для генерации уникальных идентификаторов задач
valid_statuses = {"todo", "in_progress", "done"}

class Task:
    def __init__(self, title: str, priority: str, status: str, description: str = '', deadline: date | None = None):
        if status not in valid_statuses:
            raise ValueError(f"Некорректное значение статуса: {status}. Допустимые значения: {valid_statuses}")
        self.id = next(_id_counter)  # генерация уникального идентификатора
        self.title = title
        self.priority = priority
        self.status = status
        self.description = description
        self.deadline = deadline
