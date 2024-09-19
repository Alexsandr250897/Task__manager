import pytest
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
from .models import Task

@pytest.fixture
def api_client():
    return APIClient()

@pytest.fixture
def create_task(db):
    def make_task(**kwargs):
        return Task.objects.create(**kwargs)
    return make_task



@pytest.mark.django_db
def test_create_task(api_client):
    url = reverse('tasks-list')
    data = {
        'title': 'New Task',
        'description': 'Task description',
        'status': 'in progress',
        'priority': 'high'
    }
    response = api_client.post(url, data, format='json')

    assert response.status_code == status.HTTP_201_CREATED
    assert Task.objects.count() == 1
    assert Task.objects.get().title == 'New Task'


@pytest.mark.django_db
def test_get_tasks(api_client, create_task):
    # Создадим несколько задач для теста
    create_task(title="Task 1", status="in progress", priority="high")
    create_task(title="Task 2", status="completed", priority="low")

    url = reverse('tasks-list')
    response = api_client.get(url)
    assert response.status_code == status.HTTP_200_OK
    assert len(response.data) == 2

    response = api_client.get(url, {'status': 'in progress'})
    assert len(response.data) == 1
    assert response.data[0]['title'] == 'Task 1'

    response = api_client.get(url, {'priority': 'high'})
    assert len(response.data) == 1
    assert response.data[0]['title'] == 'Task 1'


@pytest.mark.django_db
def test_get_task_by_id(api_client, create_task):
    task = create_task(title="Task 1", status="in progress", priority="high")

    url = reverse('tasks-detail', args=[task.id])
    response = api_client.get(url)

    assert response.status_code == status.HTTP_200_OK
    assert response.data['title'] == 'Task 1'
    assert response.data['status'] == 'in progress'


@pytest.mark.django_db
def test_delete_task(api_client, create_task):
    task = create_task(title="Task 1", status="in progress", priority="high")

    url = reverse('tasks-detail', args=[task.id])
    response = api_client.delete(url)

    assert response.status_code == status.HTTP_204_NO_CONTENT
    assert Task.objects.count() == 0
