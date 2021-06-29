import os
from django.contrib.auth import get_user_model
from django.core.management import BaseCommand
from django.conf import settings
from app.training.models import Solution, TaskItem
from app.tasks.models import Task
from app.groups.models import Group, GroupMember


UserModel = get_user_model()


class Command(BaseCommand):

    def handle(self, *args, **options):
        task = Task.objects.get(title='Задание')
        common_group = Group.objects.filter(
            title='Отборочный этап'
        ).first()
        taskitem = TaskItem.objects.get(task=task)
        for user in UserModel.objects.all():
            if Solution.objects.filter(user=user, taskitem=taskitem).exists():
                member, created = GroupMember.objects.get_or_create(
                    user=user,
                    group=common_group
                )
                if created:
                    self.stdout.write(self.style.SUCCESS(user.get_full_name()))
