# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2021-01-08 08:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('training', '0011_auto_20200719_1551'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='translator',
            field=models.CharField(choices=[('1', 'Python 3.8'), ('2', 'GCC 7.5')], default=1, max_length=2, verbose_name='транслятор кода'),
            preserve_default=False,
        ),
    ]
