from django.contrib.auth.models import Group
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = "Project iniatilizing"

    def handle(self, *args, **kwargs):
        members_group = Group.objects.get_or_create(name="Member")
        if members_group:
            self.stdout.write(self.style.SUCCESS("Criado grupo 'Member'."))
        managers_group = Group.objects.get_or_create(name="Manager")
        if managers_group:
            self.stdout.write(self.style.SUCCESS("Criado grupo 'Manager'."))
