from rest_framework.test import APIClient, APITestCase

from tasks.models import Task

# Create your tests here.


class TasksTestCase(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.task = Task.objects.create(
            titulo="Nova tarefa",
            descricao="Uma nova tarefa",
            deadline="2023-11-11",
            done=False,
        )

    def test_list_all_tasks(self):
        response = self.client.get("/api/tasks/")
        self.assertEqual(response.status_code, 200)

    def test_task_retrieve(self):
        response = self.client.get(f"/api/tasks/{self.task.pk}/")
        self.assertEqual(response.status_code, 200)

    def test_create_new_task(self):
        data = {
            "titulo": "Nova tarefa",
            "descricao": "Uma nova tarefa",
            "deadline": "2023-11-11",
            "done": False,
        }
        response = self.client.post("/api/tasks/", data=data)
        self.assertEqual(response.status_code, 201)

    def test_task_update(self):
        data = {
            "titulo": "Outra tarefa 1",
            "descricao": "Uma nova tarefa sendo atualizada",
            "deadline": "2023-12-12",
            "done": False,
        }
        print(self.task.pk)
        response = self.client.put(f"/api/tasks/{self.task.pk}/", data=data)
        self.assertEqual(response.status_code, 200)

    def test_partial_task_update(self):
        data = {
            "done": True,
        }
        print(self.task.pk)
        response = self.client.patch(f"/api/tasks/{self.task.pk}/", data=data)
        self.assertEqual(response.status_code, 200)

    def test_delete_task(self):
        response = self.client.delete(f"/api/tasks/{self.task.pk}/")
        self.assertEqual(response.status_code, 204)
