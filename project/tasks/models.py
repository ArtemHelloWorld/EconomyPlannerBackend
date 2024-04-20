import django.db.models
import django.urls
from django.core.validators import MinValueValidator
from django.utils import timezone

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
    deadline_start = django.db.models.DateField(
        verbose_name='начало работы',
        help_text='Укажите срок начала работы над задачи'
    )
    deadline_end = django.db.models.DateField(
        verbose_name='конец работы',
        help_text='Укажите срок окончания работы над задачи'

    )

    users = django.db.models.ManyToManyField(
        users.models.User,
        blank=True,
        related_name='tasks',
        related_query_name='tasks',
        verbose_name='исполнители',
        help_text='Выберите исполнителей задачи'
    )

    random_users_count = django.db.models.PositiveSmallIntegerField(
        default=0,
        validators=[
            MinValueValidator(0),
        ],
        verbose_name='количество случайных исполнителей',
        help_text=('Выберите количество исполнителей задачи, '
                   'которые добавятся к, уже выбранным вами исполнителям, '
                   'из числа менее загруженных сотрудников')
    )

    date_created = django.db.models.DateTimeField(
        auto_now_add=True,
        verbose_name='дата создания'
    )
    date_update = django.db.models.DateTimeField(
        auto_now=True,
        verbose_name='дата изменения'
    )
    date_completed = django.db.models.DateTimeField(
        null=True,
        blank=True,
        verbose_name='время сдачи',
        help_text='Время за которое была сдана работа'

    )

    def save(self, *args, **kwargs):
        if self.status and not self.date_completed:
            self.date_completed = timezone.now()
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = 'задача'
        verbose_name_plural = 'задачи'
        ordering = ['status', 'deadline_start', 'deadline_end', 'date_created']

    def __str__(self):
        return self.name[:20]


