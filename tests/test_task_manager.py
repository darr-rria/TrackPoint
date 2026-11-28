from trackpoint.task_manager import TaskManager
from trackpoint.models import Task

class TestTaskManager:
    def setup_method(self):
        self.task_manager = TaskManager()

    def test_add_task(self):
        task = Task("Test Task", "This is a test task.", "2023-12-31")
        self.task_manager.add_task(task)
        assert len(self.task_manager.get_all_tasks()) == 1
        assert self.task_manager.get_all_tasks()[0] == task

    def test_get_task_by_id(self):
        task1 = Task("Task 1", "First task.", "2023-12-31")
        task2 = Task("Task 2", "Second task.", "2024-01-15")
        self.task_manager.add_task(task1)
        self.task_manager.add_task(task2)

        retrieved_task = self.task_manager.get_task_by_id(task1.id)
        assert retrieved_task == task1

        retrieved_task_none = self.task_manager.get_task_by_id(999)  # Non-existent ID
        assert retrieved_task_none is None