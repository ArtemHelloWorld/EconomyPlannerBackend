from django.contrib import admin

import users.models


@admin.register(users.models.User)
class TaskAdmin(admin.ModelAdmin):
    list_display = (
        users.models.User.id.field.name,
    )
