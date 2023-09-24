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


class ManagerCreateSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=150)
    password = serializers.CharField(max_length=150)
    name = serializers.CharField(max_length=150)
    email = serializers.EmailField()


class ManagerSerializer(serializers.ModelSerializer):
    id = serializers.CharField(max_length=150)
    username = serializers.SerializerMethodField()
    name = serializers.SerializerMethodField()
    email = serializers.SerializerMethodField()

    class Meta:
        model = Manager
        fields = ["id", "name", "username", "email"]

    def get_username(self, obj):
        return obj.user.username

    def get_name(self, obj):
        return obj.user.name

    def get_email(self, obj):
        return obj.user.email


class MemberCreateSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=150)
    password = serializers.CharField(max_length=150)
    name = serializers.CharField(max_length=150)
    email = serializers.EmailField()


class MemberSerializer(serializers.ModelSerializer):
    id = serializers.CharField(max_length=150)
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
