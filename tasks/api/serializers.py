from rest_framework import serializers

from tasks.models import Task, TaskList


class TaskCreateSerializer(serializers.Serializer):
    titulo = serializers.CharField(max_length=140)
    descricao = serializers.CharField(max_length=140)
    deadline = serializers.DateField()
    done = serializers.BooleanField()
    tasklist = serializers.CharField(
        max_length=150, required=False, allow_null=True, default=None
    )


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = "__all__"


class TaskListCreateSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=140)


class TaskListSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaskList
        fields = "__all__"


class AddCollaboratorSerializer(serializers.Serializer):
    user_id = serializers.UUIDField()
    task_id = serializers.UUIDField()
