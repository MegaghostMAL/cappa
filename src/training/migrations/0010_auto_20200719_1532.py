# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-07-19 15:32
from __future__ import unicode_literals

from django.db import migrations, models


def set_last_modified(apps, schema_editor):

    """ Миграция данных, инициализация значения поля last_modified """

    from django.utils import timezone
    Solution = apps.get_model('training', 'Solution')
    for solution in Solution.objects.all():
        if solution.datetime is None:
            solution.datetime = timezone.now()
        if solution.last_modified is None:
            solution.last_modified = solution.datetime
        solution.save()


def unset_last_modified(apps, schema_editor):

    """ Миграция данных, деинициализация значения поля last_modified """

    pass


class Migration(migrations.Migration):

    dependencies = [
        ('training', '0009_taskitem_one_try'),
    ]

    operations = [
        migrations.AddField(
            model_name='solution',
            name='last_modified',
            field=models.DateTimeField(blank=True, null=True, verbose_name='дата последней отправки'),
        ),
        migrations.AlterField(
            model_name='solution',
            name='datetime',
            field=models.DateTimeField(auto_now_add=True, null=True, verbose_name='дата создания'),
        ),
        migrations.RunPython(code=set_last_modified, atomic=True, reverse_code=unset_last_modified)
    ]
