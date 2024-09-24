from django_filters import rest_framework as filters
from .models import Task


class TaskFilter(filters.FilterSet):
    created_at = filters.DateTimeFilter(field_name='created_at', lookup_expr='gte')
    status = filters.CharFilter(field_name='status', lookup_expr='icontains')
    priority = filters.CharFilter(field_name='priority', lookup_expr='icontains')

    class Meta:
        model = Task
        fields = ['status', 'created_at', 'priority']
