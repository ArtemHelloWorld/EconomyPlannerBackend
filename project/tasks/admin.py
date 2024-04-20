from django.contrib import admin
from django.db.models import Count

import tasks.models
import users.models

@admin.register(tasks.models.Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = (
        tasks.models.Task.id.field.name,
        tasks.models.Task.name.field.name,
        tasks.models.Task.status.field.name,
        tasks.models.Task.deadline_start.field.name,
        tasks.models.Task.deadline_end.field.name,
        tasks.models.Task.date_completed.field.name,
    )
    list_display_links = (
        tasks.models.Task.id.field.name,
        tasks.models.Task.name.field.name,
        tasks.models.Task.status.field.name,
        tasks.models.Task.deadline_start.field.name,
        tasks.models.Task.deadline_end.field.name,
    )
    filter_horizontal = (
        tasks.models.Task.users.field.name,
    )

    def save_model(self, request, obj, form, change):
        super().save_model(request, obj, form, change)
        if obj.random_users_count > 0:
            random_users = (
                               users.models.User.objects
                               .exclude(id__in=obj.users.all())
                               .exclude(id__in=form.cleaned_data[tasks.models.Task.users.field.name])
                               .filter(groups__name='Workers')
                               .annotate(tasks_count=Count('tasks'))
                               .order_by('tasks_count')
                           )[:obj.random_users_count]
            obj.users.add(*random_users)
            obj.users.add(*form.cleaned_data[tasks.models.Task.users.field.name])
            form.cleaned_data[tasks.models.Task.users.field.name] = obj.users.all()
            obj.random_users_count = 0
            obj.save()
            