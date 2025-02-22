# Generated by Django 3.2.12 on 2023-11-27 12:09

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('tasks', '0001_initial_squashed_0005_alter_task_name'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='task',
            options={'ordering': ['status', 'deadline_start', 'deadline_end', 'date_created'], 'verbose_name': 'задача', 'verbose_name_plural': 'задачи'},
        ),
        migrations.RemoveField(
            model_name='task',
            name='deadline',
        ),
        migrations.AddField(
            model_name='task',
            name='deadline_end',
            field=models.DateField(blank=True, help_text='Укажите срок окончания работы над задачи', null=True, verbose_name='конец работы'),
        ),
        migrations.AddField(
            model_name='task',
            name='deadline_start',
            field=models.DateField(blank=True, help_text='Укажите срок начала работы над задачи', null=True, verbose_name='начало работы'),
        ),
        migrations.AddField(
            model_name='task',
            name='random_users_count',
            field=models.PositiveSmallIntegerField(default=0, help_text='Выберите количество исполнителей задачи, которые добавятся к, уже выбранным вами исполнителям, из числа менее загруженных сотрудников', verbose_name='количество случайных исполнителей'),
        ),
        migrations.AlterField(
            model_name='task',
            name='users',
            field=models.ManyToManyField(help_text='Выберите исполнителей задачи', to=settings.AUTH_USER_MODEL, verbose_name='исполнители'),
        ),
    ]
