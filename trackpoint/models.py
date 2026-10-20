#описывает, что такое задача
class Task:
    def __init__(self, title, priority, status):
        self.title = title
        self.priority = priority
        self.status = status