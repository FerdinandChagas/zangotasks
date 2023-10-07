from rest_framework import status
from rest_framework.decorators import action
from rest_framework.exceptions import NotAuthenticated, ParseError, PermissionDenied
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from tasks.api.serializers import (
    AddCollaboratorSerializer,
    TaskCreateSerializer,
    TaskListCreateSerializer,
    TaskListSerializer,
    TaskSerializer,
)
from tasks.models import Task, TaskList
from tasks.services import TaskListService, TaskService


class TaskViewSet(ModelViewSet):
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]
    queryset = Task.objects.all()
    service = TaskService()

    def create(self, request):
        serializer = TaskCreateSerializer(data=request.data)
        try:
            serializer.is_valid()
            new_task = self.service.create(
                data=serializer.validated_data, user=request.user
            )
            serializer = TaskSerializer(new_task)

            return Response(
                {"Info": "Tafefa criada na lista!!", "data": serializer.data},
                status=status.HTTP_200_OK,
            )
        except (ParseError, ValueError):
            return Response(
                {
                    "Info": "Falha ao tentar cadastrar tarefa. Verifique as inforamções e tente novamente!"
                },
                status=status.HTTP_400_BAD_REQUEST,
            )
        except PermissionDenied:
            return Response(
                {"Info": "Operação não permitida."}, status=status.HTTP_403_FORBIDDEN
            )
        except NotAuthenticated:
            return Response(
                {"Info": "Usuário não autenticado."},
                status=status.HTTP_401_UNAUTHORIZED,
            )

    @action(methods=["post"], detail=False, url_path="collaborators")
    def add_collaborator(self, request):
        serializer = AddCollaboratorSerializer(data=request.data)
        try:
            serializer.is_valid(raise_exception=True)
            task = self.service.add_collaborator(data=serializer.validated_data)
            serializer = TaskSerializer(task)

            return Response(
                {"Info": "Colaborador adicionado na tarefa!", "data": serializer.data},
                status=status.HTTP_200_OK,
            )
        except (ParseError, ValueError):
            return Response(
                {
                    "Info": "Falha ao tentar adicionar colaborador. Verifique as inforamções e tente novamente!"
                },
                status=status.HTTP_400_BAD_REQUEST,
            )
        except PermissionDenied:
            return Response(
                {"Info": "Operação não permitida."}, status=status.HTTP_403_FORBIDDEN
            )
        except NotAuthenticated:
            return Response(
                {"Info": "Usuário não autenticado."},
                status=status.HTTP_401_UNAUTHORIZED,
            )

    @action(methods=["post"], detail=False, url_path="discollaborate")
    def remove_collaborator(self, request):
        serializer = AddCollaboratorSerializer(data=request.data)
        try:
            serializer.is_valid(raise_exception=True)
            task = self.service.remove_collaborator(data=serializer.validated_data)
            serializer = TaskSerializer(task)

            return Response(
                {"Info": "Colaborador removido na tarefa!", "data": serializer.data},
                status=status.HTTP_200_OK,
            )
        except (ParseError, ValueError):
            return Response(
                {
                    "Info": "Falha ao tentar remover colaborador. Verifique as inforamções e tente novamente!"
                },
                status=status.HTTP_400_BAD_REQUEST,
            )
        except PermissionDenied:
            return Response(
                {"Info": "Operação não permitida."}, status=status.HTTP_403_FORBIDDEN
            )
        except NotAuthenticated:
            return Response(
                {"Info": "Usuário não autenticado."},
                status=status.HTTP_401_UNAUTHORIZED,
            )


class TaskListViewSet(ModelViewSet):
    serializer_class = TaskListSerializer
    permission_classes = [AllowAny]
    queryset = TaskList.objects.all()
    service = TaskListService()

    def create(self, request):
        serializer = TaskListCreateSerializer(data=request.data)
        try:
            serializer.is_valid(raise_exception=True)
            new_tasklist = self.service.create(
                data=serializer.validated_data, user=request.user
            )
            serializer = TaskListSerializer(new_tasklist)

            return Response(
                {"Info": "Tafefa criada na lista!", "data": serializer.data},
                status=status.HTTP_200_OK,
            )
        except (ParseError, ValueError):
            return Response(
                {
                    "Info": "Falha ao tentar cadastrar lista de trarefas. Verifique as inforamções e tente novamente!"
                },
                status=status.HTTP_400_BAD_REQUEST,
            )
        except PermissionDenied:
            return Response(
                {"Info": "Operação na permitida."}, status=status.HTTP_403_FORBIDDEN
            )
        except NotAuthenticated:
            return Response(
                {"Info": "Usuário não autenticado."},
                status=status.HTTP_401_UNAUTHORIZED,
            )
