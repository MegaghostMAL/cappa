# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-07-19 15:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('training', '0010_auto_20200719_1532'),
    ]

    operations = [
        migrations.AlterField(
            model_name='solution',
            name='datetime',
            field=models.DateTimeField(auto_now_add=True, verbose_name='дата создания'),
        ),
        migrations.AlterField(
            model_name='solution',
            name='last_modified',
            field=models.DateTimeField(auto_now_add=True, verbose_name='дата последней отправки'),
        ),
    ]