from django.db import models
from core.models import BaseModel
from zangotasks.users.models import Member
# Create your models here.


class TaskList(BaseModel):
    name = models.CharField(max_length=150)

    class Meta:
        verbose_name = "Tasks List"
        verbose_name_plural = "Tasks Lists"

    def __str__(self):
        return self.name

class Task(BaseModel):
    titulo = models.CharField(max_length=150)
    descricao = models.CharField(max_length=200)
    deadline = models.DateField()
    done = models.BooleanField()
    tasklist = models.ForeignKey(TaskList, on_delete=models.CASCADE, related_name="tasks")
    collaborators = models.ManyToManyField(Member, blank=True)

    class Meta:
        verbose_name = "Tasks"
        verbose_name_plural = "Tasks"

    def __str__(self):
        return self.titulo

