import django.contrib.auth.models
import django.db.models


class UserManager(django.db.models.Manager):
    def get_queryset(self):
        return (
            super()
            .get_queryset()
            .prefetch_related('subordinates')
        )


class User(django.contrib.auth.models.AbstractUser):
    job_title = django.db.models.CharField(
        max_length=256,
        verbose_name='должность'
    )

    subordinates = django.db.models.ManyToManyField(
        'User',
        blank=True,
        related_name='bosses',
        related_query_name='bosses',
        verbose_name='подчиненные',
        help_text='Выберите подчиненных данного пользователя'
    )

    def __str__(self):
        groups = ', '.join([group.name for group in self.groups.all()])
        return f'{self.job_title} {self.username}  | Группа: {groups}'

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
        ordering = ['-date_joined', 'username']
