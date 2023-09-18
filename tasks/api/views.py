from rest_framework import status
from rest_framework.decorators import action
from rest_framework.exceptions import ParseError, PermissionDenied, NotAuthenticated
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from tasks.api.serializers import AddCollaboratorSerializer, TaskListSerializer, TaskSerializer
from tasks.models import Task, TaskList
from zangotasks.users.models import Member, User


class TaskViewSet(ModelViewSet):
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]
    queryset = Task.objects.all()

    def create(self, request):
        data = request.data
        try:
            tasklist = None
            
            try:
                tasklist = TaskList.objects.get(id=data['tasklist'])
            except TaskList.DoesNotExist:
                tasklist = TaskList.objects.create(name="Untitiled", created_by=request.user)
            
            new_task = Task.objects.create(
                titulo = data['titulo'],
                descricao = data['descricao'],
                deadline = data['deadline'],
                done = False,
                tasklist = tasklist,
                created_by = request.user,
            )
            new_task.save()
            serializer = TaskSerializer(new_task)


            return Response({"Info": "Tafefa criada na lista!", "data": serializer.data}, status=status.HTTP_200_OK)
        except (ParseError, ValueError):
            return Response({"Info": "Falha ao tentar cadastrar tarefa. Verifique as inforamções e tente novamente!"}, status=status.HTTP_400_BAD_REQUEST)
        except PermissionDenied:
            return Response({"Info": "Operação na permitida."}, status=status.HTTP_403_FORBIDDEN)
        except NotAuthenticated:
            return Response({"Info": "Usuário não autenticado."}, status=status.HTTP_401_UNAUTHORIZED)
    
    @action(methods=['post'], detail=False)
    def add_collaborator(self, request):
        data = request.data
        member = Member.objects.get(user__pk=data['user_id'])
        task = Task.objects.get(pk=data['task_id'])
        task.collaborators.add(member)
        task.save()
        serializer = TaskSerializer(task)
        return Response({"Info": "Colaborador adicionado na tarefa!", "data": serializer.data}, status=status.HTTP_200_OK)


class TaskListViewSet(ModelViewSet):
    serializer_class = TaskListSerializer
    permission_classes = [AllowAny]
    queryset = TaskList.objects.all()

    def create(self, request):
        data = request.data
        try:
            
            new_tasklist = TaskList.objects.create(
                name=data['name'],
                created_by=request.user,
            )
            new_tasklist.save()
            serializer = TaskListSerializer(new_tasklist)


            return Response({"Info": "Tafefa criada na lista!", "data": serializer.data}, status=status.HTTP_200_OK)
        except (ParseError, ValueError):
            return Response({"Info": "Falha ao tentar cadastrar lista de trarefas. Verifique as inforamções e tente novamente!"}, status=status.HTTP_400_BAD_REQUEST)
        except PermissionDenied:
            return Response({"Info": "Operação na permitida."}, status=status.HTTP_403_FORBIDDEN)
        except NotAuthenticated:
            return Response({"Info": "Usuário não autenticado."}, status=status.HTTP_401_UNAUTHORIZED)
    
    