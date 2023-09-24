from rest_framework.test import APITestCase

from tasks.models import Task
from tasks.services import TaskService
from zangotasks.users.models import User
from zangotasks.users.serivces import ManagerService

# Create your tests here.


class TasksTestCase(APITestCase):
    def setUp(self):
        self.service = TaskService()
        self.user = User.objects.create_user(username="tester", password= "senha123")

    def test_create_task(self):
        data = {
            "titulo": "Outra tarefa 1",
            "descricao": "Uma nova tarefa sendo atualizada",
            "deadline": "2023-12-12",
            "done": False,
        }
        task = self.service.create(data, self.user)
        last_task = Task.objects.all().last()
        self.assertEqual(task.titulo, last_task.titulo)