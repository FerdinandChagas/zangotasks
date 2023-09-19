from typing import Any
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.exceptions import ParseError, PermissionDenied, NotAuthenticated
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin, UpdateModelMixin, CreateModelMixin
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet, ModelViewSet

from zangotasks.users.models import Manager, Member

from .serializers import ManagerSerializer, MemberSerializer, UserSerializer

User = get_user_model()


class UserViewSet(RetrieveModelMixin, ListModelMixin, UpdateModelMixin, GenericViewSet, CreateModelMixin):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    lookup_field = "username"

    def get_queryset(self, *args, **kwargs):
        assert isinstance(self.request.user.id, int)
        return self.queryset.filter(id=self.request.user.id)

    @action(detail=False)
    def me(self, request):
        serializer = UserSerializer(request.user, context={"request": request})
        return Response(status=status.HTTP_200_OK, data=serializer.data)
    

class ManagerViewSet(ModelViewSet):
    serializer_class = ManagerSerializer
    queryset = Manager.objects.all()

    def create(self, request):
        data = request.data
        try:
            group = Group.objects.get(name="Manager")
            new_user = User.objects.create_user(
                username = data['username'],
                password = data['password'],
                email = data['email'],
                name = data['name'],
            )
            new_user.groups.add(group)
            new_user.save()
            new_manager = Manager.objects.create(user=new_user)
            new_manager.save()
            serializer = ManagerSerializer(new_manager)
            return Response({"Info": "Manager criado!", "data": serializer.data}, status=status.HTTP_201_CREATED)
        except ParseError:
            return Response({"Info": "Falha ao tentar cadastrar manager. Verifique as inforamções e tente novamente!"}, status=status.HTTP_400_BAD_REQUEST)
        except PermissionDenied:
            return Response({"Info": "Operação na permitida."}, status=status.HTTP_403_FORBIDDEN)
        except NotAuthenticated:
            return Response({"Info": "Usuário não autenticado."}, status=status.HTTP_401_UNAUTHORIZED)

class MemberViewSet(ModelViewSet):
    serializer_class = MemberSerializer
    queryset = Member.objects.all()

    def create(self, request):
        data = request.data
        try:
            group = Group.objects.get(name="Member")
            new_user = User.objects.create_user(
                username = data['username'],
                password = data['password'],
                email = data['email'],
                name = data['name'],
            )
            new_user.groups.add(group)
            new_user.save()
            new_member = Member.objects.create(user=new_user)
            new_member.save()
            serializer = MemberSerializer(new_member)
            return Response({"Info": "Member criado!", "data": serializer.data}, status=status.HTTP_201_CREATED)
        except ParseError:
            return Response({"Info": "Falha ao tentar cadastrar member. Verifique as inforamções e tente novamente!"}, status=status.HTTP_400_BAD_REQUEST)
        except PermissionDenied:
            return Response({"Info": "Operação na permitida."}, status=status.HTTP_403_FORBIDDEN)
        except NotAuthenticated:
            return Response({"Info": "Usuário não autenticado."}, status=status.HTTP_401_UNAUTHORIZED)

        
