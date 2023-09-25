from tasks.models import Task, TaskList
from zangotasks.users.models import Member


class TaskService:
    def create(self, data, user):
        tasklist = None
        try:
            tasklist = TaskList.objects.get(id=data["tasklist"])
        except (TaskList.DoesNotExist, KeyError):
            tasklist = TaskList.objects.create(name="Untitiled", created_by=user)

        new_task = Task.objects.create(
            titulo=data["titulo"],
            descricao=data["descricao"],
            deadline=data["deadline"],
            done=False,
            tasklist=tasklist,
            created_by=user,
        )
        new_task.save()
        return new_task

    def add_collaborator(self, data):
        member = Member.objects.get(user__pk=data["user_id"])
        task = Task.objects.get(pk=data["task_id"])
        task.collaborators.add(member)
        task.save()
        return task


class TaskListService:
    def create(self, data, user):
        new_tasklist = TaskList.objects.create(
            name=data["name"],
            created_by=user,
        )
        new_tasklist.save()
        return new_tasklist
