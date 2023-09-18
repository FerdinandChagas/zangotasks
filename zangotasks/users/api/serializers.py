from django.contrib.auth import get_user_model
from rest_framework import serializers

from zangotasks.users.models import Manager, Member

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["username", "name", "url"]

        extra_kwargs = {
            "url": {"view_name": "api:user-detail", "lookup_field": "username"}
        }

class ManagerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Manager
        fields = ["id", "username", "password", "name", "email"]


class MemberSerializer(serializers.ModelSerializer):
    username = serializers.SerializerMethodField()
    name = serializers.SerializerMethodField()
    email = serializers.SerializerMethodField()

    class Meta:
        model = Member
        fields = ["id", "username", "name", "email"]

    def get_username(self, obj):
        return obj.user.username
    
    def get_name(self, obj):
        return obj.user.name
    
    def get_email(self, obj):
        return obj.user.email