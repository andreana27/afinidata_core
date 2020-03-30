from messenger_users.models import User as MessengerUser
from django.contrib.auth.models import User
from programs.models import Program
from django.db import models
from bots.models import Bot


ROLE_CHOICES = (('administrator', 'Administrator'), ('collaborator', 'Collaborator'))


class Group(models.Model):
    name = models.CharField(max_length=20, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    available = models.BooleanField(default=True)
    bots = models.ManyToManyField(Bot, through='BotAssignation')
    programs = models.ManyToManyField(Program, through='ProgramAssignation')
    users = models.ManyToManyField(User, through='RoleGroupUser')


class RoleGroupUser(models.Model):
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)


class Code(models.Model):
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    code = models.CharField(max_length=50, unique=True)
    available = models.BooleanField(default=True)
    exchanges = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.code

    def exchange(self):
        self.exchanges = self.exchanges + 1
        self.save()


class AssignationMessengerUser(models.Model):
    messenger_user_id = models.IntegerField()
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    code = models.ForeignKey(Code, null=True, on_delete=models.SET_NULL)

    def get_messenger_user(self):
        return MessengerUser.objects.get(id=self.messenger_user_id)


class BotAssignation(models.Model):
    bot = models.ForeignKey(Bot, on_delete=models.CASCADE)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True)


class ProgramAssignation(models.Model):
    program = models.ForeignKey(Program, on_delete=models.CASCADE)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
