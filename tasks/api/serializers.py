from rest_framework import serializers

from tasks.models import Task, TaskList
from zangotasks.users.api.serializers import MemberSerializer
from zangotasks.users.models import User


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = "__all__"


class TaskListSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaskList
        fields = "__all__"

class AddCollaboratorSerializer(serializers.Serializer):

    user_id = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    task_id = serializers.PrimaryKeyRelatedField(queryset=Task.objects.all())