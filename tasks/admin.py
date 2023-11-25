from django.contrib import admin

import tasks.models


@admin.register(tasks.models.Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = (
        tasks.models.Task.id.field.name,
    )
