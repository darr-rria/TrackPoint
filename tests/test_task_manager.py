from trackpoint.task_manager import TaskManager

class TestTaskManager:
    def test_add_task(self):
        task_manager = TaskManager()
        task = Task("Test Task", "This is a test task.", "2023-12-31")
        task_manager.add_task(task)
        assert len(task_manager.get_all_tasks()) == 1
        assert task_manager.get_all_tasks()[0].title == "Test Task"

    def test_get_all_tasks(self):
        task_manager = TaskManager()
        task1 = Task("Task 1", "Description 1", "2023-12-31")
        task2 = Task("Task 2", "Description 2", "2024-01-15")
        task_manager.add_task(task1)
        task_manager.add_task(task2)
        tasks = task_manager.get_all_tasks()
        assert len(tasks) == 2
        assert tasks[0].title == "Task 1"
        assert tasks[1].title == "Task 2"

    def test_get_task_by_id(self):
        task_manager = TaskManager()
        task1 = Task("Task 1", "Description 1", "2023-12-31")
        task2 = Task("Task 2", "Description 2", "2024-01-15")
        task_manager.add_task(task1)
        task_manager.add_task(task2)
        retrieved_task = task_manager.get_task_by_id(task1.id)
        assert retrieved_task is not None
        assert retrieved_task.title == "Task 1"

    def test_get_task_by_id_not_found(self):
        task_manager = TaskManager()
        task1 = Task("Task 1", "Description 1", "2023-12-31")
        task_manager.add_task(task1)
        retrieved_task = task_manager.get_task_by_id(999)  # ID that doesn't exist
        assert retrieved_task is None

