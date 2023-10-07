from django.contrib.auth.models import Group
from rest_framework.test import APITestCase

from tasks.models import Task
from tasks.services import TaskListService, TaskService
from zangotasks.users.serivces import ManagerService, MemberService

# Create your tests here.


class TasksTestCase(APITestCase):
    def setUp(self):
        self.task_service = TaskService()
        self.member_service = MemberService()

        Group.objects.get_or_create(name="Member")
        Group.objects.get_or_create(name="Manager")

        manager_service = ManagerService()
        manager_data = {
            "username": "manager",
            "password": "manageruser",
            "name": "John Manager",
            "email": "manager@zangotasks.com",
        }
        self.user = manager_service.create(manager_data)
        self.tasklist = TaskListService().create(
            {"name": "Test-ToDO-List"}, self.user.user
        )
        task_data = {
            "titulo": "Exemplo Task 01",
            "descricao": "Uma nova tarefa sendo atualizada",
            "deadline": "2023-12-12",
            "done": False,
            "tasklist": self.tasklist.id,
        }
        self.task = self.task_service.create(task_data, self.user.user)

    def test_create_task(self):
        data = {
            "titulo": "Exemplo Task 02",
            "descricao": "Uma nova tarefa sendo atualizada",
            "deadline": "2023-12-12",
            "done": False,
            "tasklist": self.tasklist.id,
        }
        task = self.task_service.create(data, self.user.user)
        last_task = Task.objects.get(id=task.id)
        self.assertEqual(task.id, last_task.id)
        self.assertEqual(task.titulo, last_task.titulo)

    def test_add_collaborator(self):
        data_collaborator = {
            "username": "collaborator",
            "password": "collab123",
            "name": "John Wick",
            "email": "collaborator@zangotasks.com",
        }
        collaborator = self.member_service.create(data_collaborator)
        data_add_collaborator = {
            "user_id": collaborator.id,
            "task_id": self.task.id,
        }
        self.task_service.add_collaborator(data_add_collaborator)
        self.assertEqual(collaborator.id, self.task.collaborators.all().last().id)


class TaskListTestCase(APITestCase):
    def setUp(self):
        self.task_service = TaskService()
        self.member_service = MemberService()

        Group.objects.get_or_create(name="Member")
        Group.objects.get_or_create(name="Manager")

        manager_service = ManagerService()
        manager_data = {
            "username": "manager",
            "password": "manageruser",
            "name": "John Manager",
            "email": "manager@zangotasks.com",
        }
        self.user = manager_service.create(manager_data)
