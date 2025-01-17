# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-11-21 10:24
from __future__ import unicode_literals

from django.conf import settings
import django.contrib.postgres.fields.jsonb
from django.db import migrations, models
import django.db.models.deletion
import app.utils.fields
import tinymce.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('tasks', '0002_auto_20191117_1332'),
    ]

    operations = [
        migrations.CreateModel(
            name='Content',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('input', models.TextField(blank=True, null=True, verbose_name='Ввод')),
                ('content', models.TextField(blank=True, null=True, verbose_name='Редактор')),
                ('show_input', models.BooleanField(default=False, verbose_name='Отображать ввод')),
                ('show_debug', models.BooleanField(default=True, verbose_name='Отображать отладчик')),
                ('readonly', models.BooleanField(default=False, verbose_name='Только для чтения')),
                ('text', tinymce.models.HTMLField(blank=True, null=True)),
                ('type', models.CharField(choices=[('ace', 'код'), ('text', 'текст')], default='text', max_length=255, verbose_name='тип')),
                ('order_key', app.utils.fields.OrderField(blank=True, verbose_name='порядок')),
            ],
            options={
                'verbose_name': 'блок контента',
                'verbose_name_plural': 'блоки контента',
                'ordering': ['order_key'],
            },
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('show', models.BooleanField(default=True, verbose_name='отображать')),
                ('title', models.CharField(max_length=255, verbose_name='заголовок')),
                ('slug', models.SlugField(max_length=255, unique=True, verbose_name='слаг')),
                ('about', tinymce.models.HTMLField(blank=True, default='', null=True, verbose_name='краткое описание')),
                ('content', tinymce.models.HTMLField(blank=True, default='', null=True, verbose_name='текстовый контент')),
                ('content_bottom', tinymce.models.HTMLField(blank=True, default='', null=True, verbose_name='текстовый контент под списком тем')),
                ('order_key', app.utils.fields.OrderField(blank=True, null=True, verbose_name='порядок')),
                ('last_modified', models.DateTimeField(auto_now=True, verbose_name='дата последнего изменения')),
                ('author', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='автор')),
            ],
            options={
                'verbose_name': 'учебный курс',
                'verbose_name_plural': 'учебные курсы',
                'ordering': ['order_key'],
            },
        ),
        migrations.CreateModel(
            name='Solution',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('0', 'нет попыток'), ('1', 'нет прогресса'), ('2', 'есть прогресс'), ('3', 'решено')], default='0', max_length=255, verbose_name='статус')),
                ('progress', models.PositiveIntegerField(blank=True, null=True, verbose_name='Прогресс решения')),
                ('last_changes', models.TextField(blank=True, default='', verbose_name='последние изменения')),
                ('version_best', django.contrib.postgres.fields.jsonb.JSONField(blank=True, null=True, verbose_name='лучшее решение')),
                ('version_list', django.contrib.postgres.fields.jsonb.JSONField(blank=True, default=list, null=True, verbose_name='список сохраненных решений')),
            ],
            options={
                'verbose_name': 'решение задачи',
                'verbose_name_plural': 'решения задач',
            },
        ),
        migrations.CreateModel(
            name='TaskItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('show', models.BooleanField(default=True, verbose_name='отображать')),
                ('slug', app.utils.fields.SlugField(blank=True, max_length=255, null=True, verbose_name='слаг')),
                ('order_key', app.utils.fields.OrderField(blank=True, null=True, verbose_name='порядок')),
                ('task', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='topics', to='tasks.Task', verbose_name='задача')),
            ],
            options={
                'verbose_name': 'задача',
                'verbose_name_plural': 'задачи',
                'ordering': ['order_key'],
            },
        ),
        migrations.CreateModel(
            name='Topic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('show', models.BooleanField(default=True, verbose_name='отображать')),
                ('title', models.CharField(max_length=255, verbose_name='заголовок')),
                ('slug', models.SlugField(max_length=255, verbose_name='слаг')),
                ('order_key', app.utils.fields.OrderField(blank=True, null=True, verbose_name='порядок')),
                ('last_modified', models.DateTimeField(auto_now=True, verbose_name='дата последнего изменения')),
                ('author', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='автор')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='_topics', to='training.Course', verbose_name='курс')),
            ],
            options={
                'verbose_name': 'тема',
                'verbose_name_plural': 'темы',
                'ordering': ['order_key'],
            },
        ),
        migrations.AddField(
            model_name='taskitem',
            name='topic',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='_taskitems', to='training.Topic', verbose_name='тема'),
        ),
        migrations.AddField(
            model_name='solution',
            name='taskitem',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='_solution', to='training.TaskItem', verbose_name='задача'),
        ),
        migrations.AddField(
            model_name='solution',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='пользователь'),
        ),
        migrations.AddField(
            model_name='content',
            name='topic',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='_content', to='training.Topic'),
        ),
    ]
