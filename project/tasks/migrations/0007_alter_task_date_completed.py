# Generated by Django 3.2.12 on 2023-12-03 20:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0006_auto_20231203_1938'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='date_completed',
            field=models.DurationField(blank=True, help_text='Время за которое была сдана работа', null=True, verbose_name='время сдачи'),
        ),
    ]
