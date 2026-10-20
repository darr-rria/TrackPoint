# описывает, что такое задача

from datetime import date
from itertools import count

_id_counter = count(1)  # счетчик для генерации уникальных идентификаторов задач

class Task:
    def __init__(self, title: str, priority: str, status, description: str ='', deadline: date | None = None):
        self.id = next(_id_counter)  # генерация уникального идентификатора
        self.title = title
        self.priority = priority
        self.status = status
        self.description = description
        self.deadline = deadline
