from rest_framework.serializers import ModelSerializer
from tasks.models import Task, TaskList


class TaskSerializer(ModelSerializer):
    class Meta:
        model = Task
        fields = "__all__"


class TaskListSerializer(ModelSerializer):
    class Meta:
        model = TaskList
        fields = "__all__"
