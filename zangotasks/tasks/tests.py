from rest_framework.test import APIClient, APITestCase

# Create your tests here.


class TasksTestCase(APITestCase):
    def setUp(self):
        self.client = APIClient()
