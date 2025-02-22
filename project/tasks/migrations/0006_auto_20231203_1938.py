# Generated by Django 3.2.12 on 2023-12-03 16:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0005_alter_task_users'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='date_completed',
            field=models.DateTimeField(blank=True, help_text='Дата сдачи работы', null=True, verbose_name='дата сдачи'),
        ),
        migrations.AlterField(
            model_name='task',
            name='date_created',
            field=models.DateTimeField(auto_now_add=True, verbose_name='дата создания'),
        ),
        migrations.AlterField(
            model_name='task',
            name='date_update',
            field=models.DateTimeField(auto_now=True, verbose_name='дата изменения'),
        ),
    ]
