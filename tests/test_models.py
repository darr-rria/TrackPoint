from trackpoint.models import Task

def test_init():
    task = Task("Test Task", "High", "todo", "This is a test task.", None)
    assert task.title == "Test Task"
    assert task.priority == "High"
    assert task.status == "todo"
    assert task.description == "This is a test task."
    assert task.deadline is None