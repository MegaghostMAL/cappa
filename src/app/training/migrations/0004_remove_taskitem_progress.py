# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-03-30 12:28
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('training', '0003_auto_20200330_1227'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='solution',
            name='progress',
        ),
    ]