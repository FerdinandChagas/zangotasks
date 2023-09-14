from django.contrib import admin

from zangotasks.tasks.models import Task, TaskList

# Register your models here.

admin.site.register(Task)
admin.site.register(TaskList)
