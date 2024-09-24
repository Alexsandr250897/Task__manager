import pytest
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
from .models import Task
from .serializers import TaskSerializer



@pytest.mark.django_db
class TestTaskApi:
    def test_create_task(self,client,user):
        client.force_authenticate(user=user)
        data = {
            'title': 'Test Task',
            'description': 'Test Task Description',
            'status': 'new',
            'priority': 'medium'
        }

        response = client.post(reverse('task-list'), data=data, format='json')
        assert response.status_code ==status.HTTP_201_CREATED
        assert Task.objects.count() == 1
        assert TaskSerializer(Task.objects.first()).data == data

    def test_get_task_list(self, client, user, task):
        client.force_authenticate(user=user)
        response = client.get(reverse('task_list'))
        assert response.status_code == status.HTTP_200_OK
        assert len(response.data) == 1
        assert response.data[0] ['title'] == task.title


    def test_get_task_by_id(self, client, task, user):
        client.force_authenticate(user=user)
        response = client.get(reverse('task-detail',args=task.id))
        assert response.status_code == status.HTTP_200_OK
        assert response.data['title'] == task.title


    def test_update_task(self, client, task, user):
        client.force_authenticate(user=user)
        data ={'title':'updated task'}
        response = client.put(reverse('task-detail',args=[task.id]),data=data, format='json')
        assert response.status_code ==status.HTTP_200_OK
        assert Task.objects.get(id=task.id).title == 'updated task'


    def test_delete_task(self, task, user, client):
        client.force_authenticate(user=user)
        response = client.delete(reverse('task-detail',args=[task.id]))
        assert response.status_code == status.HTTP_204_NO_CONTENT
        assert Task.objects.count() == 0


    def test_filter_task_by_priority(self, task, user, client):
        client.force_authenticate(user=user)
        response = client.get(reverse('task-list') + 'priority=high')
        assert response.status_code == status.HTTP_200_OK
        assert  len(response.data) == 1

    def test_filter_task_by_created_at(self, task, user, client):
        client.force_authenticate(user=user)
        response = client.get(reverse('task-list') + f'created-at={task.created_at.isoformat()}')
        assert response.status_code == status.HTTP_200_OK
        assert len(response.data) == 1



    def test_pagination(self,task, user, client ):
        client.force_authenticate(user=user)
        response = client.get(reverse('task-list') + 'page=1')
        assert response.status_code == status.HTTP_200_OK
        assert len(response.data) == 10
        assert response.data[0]['title'] == task[0].title


@pytest.fixture
def user():
    user = User.objects.create_user(username='testuser', password='testpassword')
    return user


@pytest.fixture
def client(user):
    client = APIClient()
    tokens = get_tokens_for_user(user)
    client.credentials(HTTTP_AUTHORIZATION='Bearer' + tokens['access'])
    return client


