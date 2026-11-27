from trackpoint.models import Task

def test_init():
    task = Task("Test Task", "This is a test task.", "2023-12-31")
    assert task.title == "Test Task"
    assert task.description == "This is a test task."
    assert task.deadline == "2023-12-31"
    assert task.status == "Pending"