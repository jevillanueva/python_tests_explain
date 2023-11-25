import pytest
from datetime import datetime, timedelta
from app.task import Task, DueDateError

def is_available_to_skip():
    return True

class TestTask:
    @pytest.mark.news
    def test_task(self):
        assert True

    @pytest.mark.news
    def test_new_task(self):
        due_date = datetime.now() + timedelta(days=1)
        task = Task("Title", "Description", "jevillanueva", due_date)
        assert task.title == "Title"
        assert task.description == "Description"
        assert task.assigned_to == "jevillanueva"
        assert task.due_date == due_date

    @pytest.mark.due_date
    @pytest.mark.errors
    def test_due_date_error (self):
        with pytest.raises(DueDateError):
            due_date = datetime.now() - timedelta(days=1)
            Task("Title", "Description", "jevillanueva", due_date)
    
    @pytest.mark.due_date
    def test_due_date(self):
        due_date = datetime.now() + timedelta(days=1)
        task = Task("Title", "Description", "jevillanueva", due_date)
        assert task.due_date > datetime.now()

    #skip
    #skipIf

    @pytest.mark.skip(reason="No se necesita probar")
    def test_skip(self):
        pass

    @pytest.mark.skipif(is_available_to_skip(), reason="No cumple la condición")
    def test_skipif(self):
        pass

    # Parametrización
    @pytest.mark.news
    @pytest.mark.parametrize(
        "title, description, assigned_to, due_date",
        [
            ("Title 1", "Description", "jevillanueva", datetime.now() + timedelta(days=1)),
            ("Title 2", "Description", "jevillanueva", datetime.now() + timedelta(days=2)),
            ("Title 3", "Description", "jevillanueva", datetime.now() + timedelta(days=3)),
            ("Title 4", "Description", "jevillanueva", datetime.now() + timedelta(days=4)),
            ("Title 5", "Description", "jevillanueva", datetime.now() + timedelta(days=5)),
            ("Title 7", "Description", "jevillanueva", datetime.now() + timedelta(days=6)),
        ]
    )
    def test_new_task_parametrize(self, title, description, assigned_to, due_date):
        task = Task(title, description, assigned_to, due_date)
        assert task.title == title
        assert task.description == description
        assert task.assigned_to == assigned_to
        assert task.due_date == due_date

@pytest.fixture
def username():
    return "jevillanueva"

@pytest.fixture
def password():
    return "123456"

def test_username(username):
    print (username)
    assert username == "jevillanueva"

def test_username_and_password(username, password):
    assert username == "jevillanueva"
    assert password == "123456" 

@pytest.fixture
def username2():
    print (">> Antes de la prueba")
    yield "jevillanueva"
    print (">> Despues de la prueba")

def test_username2(username2):
    print (username2)
    assert username2 == "jevillanueva"