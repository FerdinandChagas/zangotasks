from django.contrib.auth.models import Group

from zangotasks.users.models import Manager, Member, User


class ManagerService:
    def create(self, data):
        group = Group.objects.get(name="Manager")
        new_user = User.objects.create_user(
            username=data["username"],
            password=data["password"],
            email=data["email"],
            name=data["name"],
        )
        new_user.groups.add(group)
        new_user.save()
        new_manager = Manager.objects.create(user=new_user)
        new_manager.save()
        return new_manager


class MemberService:
    def create(self, data):
        group = Group.objects.get(name="Member")
        new_user = User.objects.create_user(
            username=data["username"],
            password=data["password"],
            email=data["email"],
            name=data["name"],
        )
        new_user.groups.add(group)
        new_user.save()
        new_member = Member.objects.create(user=new_user)
        new_member.save()
        return new_member
