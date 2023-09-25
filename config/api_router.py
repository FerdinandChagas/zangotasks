from django.conf import settings
from rest_framework.routers import DefaultRouter, SimpleRouter

from tasks.api.views import TaskListViewSet, TaskViewSet
from zangotasks.users.api.views import ManagerViewSet, MemberViewSet, UserViewSet

if settings.DEBUG:
    router = DefaultRouter()
else:
    router = SimpleRouter()

router.register("users", UserViewSet)
router.register("tasks", TaskViewSet)
router.register("tasklist", TaskListViewSet)
router.register("members", MemberViewSet)
router.register("managers", ManagerViewSet)


app_name = "api"
urlpatterns = router.urls
