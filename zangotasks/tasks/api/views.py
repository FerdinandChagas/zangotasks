from rest_framework.permissions import AllowAny
from rest_framework.viewsets import ModelViewSet

from tasks.api.serializers import TaskListSerializer, TaskSerializer
from tasks.models import Task, TaskList


class TaskViewSet(ModelViewSet):
    serializer_class = TaskSerializer
    permission_classes = [AllowAny]
    queryset = Task.objects.all()


class TaskListViewSet(ModelViewSet):
    serializer_class = TaskListSerializer
    permission_classes = [AllowAny]
    queryset = TaskList.objects.all()