from datetime import datetime


class DueDateError(Exception):
    pass


class Task:
    def __init__(self, title, description, assigned_to, due_date, status="PENDING") -> None:
        self.title = title
        self.description = description
        self.assigned_to = assigned_to
        if due_date < datetime.now():
            raise DueDateError("La fecha de vencimiento no puede ser menor a la fecha actual")
        self.due_date = due_date

    def done(self):
        self.status = "DONE"

    def undone(self):
        self.status = "PENDING"