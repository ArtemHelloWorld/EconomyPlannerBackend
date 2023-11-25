import django.db.models
import django.urls

import users.models


class Task(django.db.models.Model):
    name = django.db.models.CharField(
        max_length=100,
        verbose_name='название',
        help_text='Укажите название задачи'
    )
    status = django.db.models.BooleanField(
        default=False,
        verbose_name='статус',
        help_text='Статус выполнения задачи'
    )
    deadline = django.db.models.DateField(
        null=True,
        blank=True,
        verbose_name='дедлайн',
        help_text='Укажите срок сдачи задачи'
    )
    users = django.db.models.ManyToManyField(
        users.models.User,
        verbose_name='исполняющий',
        help_text='Выберите исполнителей задачи'
    )

    date_created = django.db.models.DateField(
        auto_now_add=True,
        verbose_name='дата создания'
    )
    date_update = django.db.models.DateField(
        auto_now=True,
        verbose_name='дата изменения'
    )

    class Meta:
        verbose_name = 'задача'
        verbose_name_plural = 'задачи'
        ordering = ['-deadline', '-status', '-date_created']

    def __str__(self):
        return self.name[:20]
