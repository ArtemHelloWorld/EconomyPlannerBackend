import django.contrib.auth.models
import django.db.models


class User(django.contrib.auth.models.AbstractUser):
    job_title = django.db.models.CharField(
        max_length=256,
        verbose_name='должность'
    )

    def __str__(self):
        return f'Пользователь {self.pk}'

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
        ordering = ['-date_joined', 'username']