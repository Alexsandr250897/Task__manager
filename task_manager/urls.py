from django.contrib import admin
from django.urls import path, include

import tasks.views


urlpatterns = [
    path('', tasks.views.TaskListView.as_view(), name='home'),
    path("admin/", admin.site.urls),
    path('tasks/', include('tasks.urls')),
]
