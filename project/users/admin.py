from django.contrib import admin

import users.models


@admin.register(users.models.User)
class TaskAdmin(admin.ModelAdmin):
    list_display = (
        users.models.User.id.field.name,
        users.models.User.username.field.name,
        users.models.User.job_title.field.name,
    )
    list_display_links = (
        users.models.User.id.field.name,
        users.models.User.username.field.name,
    )
    filter_horizontal = (
        users.models.User.groups.field.name,
        users.models.User.subordinates.field.name,
    )

