# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2021-07-20 09:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0003_auto_20190901_1620'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='news',
            options={'ordering': ['-date'], 'verbose_name': 'запись на стене', 'verbose_name_plural': 'записи на стене'},
        ),
        migrations.AddField(
            model_name='news',
            name='card_type',
            field=models.CharField(choices=[('horizontal', 'горизонтальная'), ('vertical', 'вертикальная')], default='horizontal', help_text='у горизонтальной карточки фото расположено слева от текста, у вертикальной карточки фото находится над текстом', max_length=10, verbose_name='тип карточки'),
        ),
        migrations.AlterField(
            model_name='news',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='', verbose_name='изображение'),
        ),
    ]