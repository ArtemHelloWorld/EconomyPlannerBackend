from django.contrib import admin
from django.urls import path, include
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

import tasks.views


schema_view = get_schema_view(
    openapi.Info(
        title='openApi',
        default_version='v1'
    ),
    public=True
)


urlpatterns = [
    path('admin/', admin.site.urls),

    path('api/v1/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/v1/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    path('api/v1/tasks/', tasks.views.TaskList.as_view(), name='task-list-create'),
    path('api/v1/task/<int:task_pk>', tasks.views.TaskDetail.as_view(), name='task-update-delete'),

    path('api/v1/docs', schema_view.with_ui('swagger'))
]
