from django.db import models

# Create your models here.


class Task(models.Model):
    titulo = models.CharField(max_length=150)
    descricao = models.CharField(max_length=200)
    start_date = models.DateField(null=True)
    deadline = models.DateField()
    done = models.BooleanField()

    class Meta:
        verbose_name = "Task"
        verbose_name_plural = "Tasks"

    def __str__(self):
        return self.titulo


class TaskList(models.Model):
    name = models.CharField(max_length=150)
    tasks = models.ManyToManyField(Task, blank=True)

    class Meta:
        verbose_name = "Tasks List"
        verbose_name_plural = "Tasks Lists"

    def __str__(self):
        return self.name
