# -*- coding:utf-8 -*-
from django.db import models
from django.contrib.auth.models import User
from tinymce.models import HTMLField
from app.news.entities import CardType


class News(models.Model):

    class Meta:
        verbose_name = "запись на стене"
        verbose_name_plural = "записи на стене"
        ordering = ['-date']

    show = models.BooleanField(verbose_name='показывать', default=False)
    title = models.CharField(verbose_name='заголовок', max_length=255)
    date = models.DateField(verbose_name='дата создания')
    content = HTMLField(verbose_name="описание", blank=True, null=True)
    author = models.ForeignKey(
        User, on_delete=models.SET_NULL,
        verbose_name='автор',
        blank=True, null=True
    )
    card_type = models.CharField(
        verbose_name='тип карточки',
        choices=CardType.CHOICES,
        max_length=10,
        default=CardType.HORIZONTAL,
        help_text=(
            'у горизонтальной карточки фото расположено слева от текста, '
            'у вертикальной карточки фото находится над текстом'
        )
    )
    image = models.ImageField(
        verbose_name='изображение',
        blank=True, null=True
    )

    def __str__(self):
        return self.title
