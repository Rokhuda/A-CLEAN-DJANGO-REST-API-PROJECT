import pytest
from pytest_bdd import scenarios, given, when, then
from django.urls import reverse
from rest_framework.test import APIClient
from django.contrib.auth import get_user_model
from app.domain.models import Task

scenarios('task.feature')

@pytest.fixture
def api_client():
    return APIClient()

@pytest.fixture
def user(db):
    User = get_user_model()
    return User.objects.create_user(username='bdduser', password='bddpass')

@pytest.fixture
def task_context():
    return {}

@given('a logged in user')
def a_logged_in_user(api_client, user, task_context):
    api_client.force_authenticate(user=user)
    task_context['client'] = api_client
    task_context['user'] = user
    return task_context

@when('the user creates a task')
def the_user_creates_a_task(task_context):
    client = task_context['client']
    response = client.post(reverse('task-list'), {
        'title': 'BDD Task',
        'description': 'BDD description',
        'priority': 'medium',
    })
    task_context['create_response'] = response
    task_context['task_id'] = response.data.get('id')

@then('the task is created')
def the_task_is_created(task_context):
    response = task_context['create_response']
    assert response.status_code == 201
    assert task_context['task_id'] is not None

@when('the user reads the task')
def the_user_reads_the_task(task_context):
    client = task_context['client']
    task_id = task_context['task_id']
    response = client.get(reverse('task-detail', args=[task_id]))
    task_context['read_response'] = response

@then('the task details are correct')
def the_task_details_are_correct(task_context):
    response = task_context['read_response']
    assert response.status_code == 200
    assert response.data['title'] == 'BDD Task'
    assert response.data['description'] == 'BDD description'
    assert response.data['priority'] == 'medium'

@when('the user updates the task')
def the_user_updates_the_task(task_context):
    client = task_context['client']
    task_id = task_context['task_id']
    response = client.patch(reverse('task-detail', args=[task_id]), {'completed': True})
    task_context['update_response'] = response

@then('the task is updated')
def the_task_is_updated(task_context):
    response = task_context['update_response']
    assert response.status_code == 200
    assert response.data['completed'] is True

@when('the user deletes the task')
def the_user_deletes_the_task(task_context):
    client = task_context['client']
    task_id = task_context['task_id']
    response = client.delete(reverse('task-detail', args=[task_id]))
    task_context['delete_response'] = response

@then('the task is deleted')
def the_task_is_deleted(task_context):
    response = task_context['delete_response']
    assert response.status_code == 204
    assert Task.objects.filter(id=task_context['task_id']).count() == 0
