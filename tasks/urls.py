from django.urls import path, include
from rest_framework import routers
from tasks.views import TaskViewSet


router = routers.DefaultRouter()
router.register(r'tasks', TaskViewSet)



urlpatterns = [
    path('', include(router.urls)),
    ]
