import uuid
from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.exceptions import NotAuthenticated, ParseError, PermissionDenied
from rest_framework.mixins import (
    CreateModelMixin,
    ListModelMixin,
    RetrieveModelMixin,
    UpdateModelMixin,
)
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet, ModelViewSet

from zangotasks.users.api.serializers import (
    ManagerCreateSerializer,
    ManagerSerializer,
    MemberCreateSerializer,
    MemberSerializer,
    UserSerializer,
)
from zangotasks.users.models import Manager, Member
from zangotasks.users.serivces import ManagerService, MemberService

User = get_user_model()


class UserViewSet(
    RetrieveModelMixin,
    ListModelMixin,
    UpdateModelMixin,
    GenericViewSet,
    CreateModelMixin,
):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    lookup_field = "username"

    def get_queryset(self, *args, **kwargs):
        assert isinstance(self.request.user.id, uuid.UUID)
        return self.queryset.filter(id=self.request.user.id)

    @action(detail=False)
    def me(self, request):
        serializer = UserSerializer(request.user, context={"request": request})
        return Response(status=status.HTTP_200_OK, data=serializer.data)


class ManagerViewSet(ModelViewSet):
    serializer_class = ManagerSerializer
    queryset = Manager.objects.all()
    service = ManagerService()

    def create(self, request, *args, **kwargs):
        serializer = ManagerCreateSerializer(data=request.data)
        try:
            serializer.is_valid(raise_exception=True)
            new_manager = self.service.create(data=serializer.validated_data)
            serializer = ManagerSerializer(new_manager)
            return Response(
                {"Info": "Manager criado!", "data": serializer.data},
                status=status.HTTP_201_CREATED,
            )
        except ParseError:
            return Response(
                {
                    "Info": "Falha ao tentar cadastrar manager. Verifique as inforamções e tente novamente!"
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


class MemberViewSet(ModelViewSet):
    serializer_class = MemberSerializer
    queryset = Member.objects.all()
    service = MemberService()

    def create(self, request, *args, **kwargs):
        serializer = MemberCreateSerializer(data=request.data)
        try:
            serializer.is_valid(raise_exception=True)
            new_member = self.service.create(data=serializer.validated_data)
            serializer = MemberSerializer(new_member)
            return Response(
                {"Info": "Member criado!", "data": serializer.data},
                status=status.HTTP_201_CREATED,
            )
        except ParseError:
            return Response(
                {
                    "Info": "Falha ao tentar cadastrar member. Verifique as inforamções e tente novamente!"
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
