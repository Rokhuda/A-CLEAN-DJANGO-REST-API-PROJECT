import pytest
from django.urls import reverse
from rest_framework.test import APIClient
from django.contrib.auth import get_user_model
from app.domain.models import Project


@pytest.mark.django_db
def test_project_crud_flow():
    client = APIClient()
    User = get_user_model()
    user = User.objects.create_user(username='projectuser', password='testpass')
    client.force_authenticate(user=user)

    response = client.post(reverse('project-list'), {
        'name': 'Test Project',
        'description': 'Project description',
        'is_archived': False,
    })
    assert response.status_code == 201
    project_id = response.data['id']

    response = client.get(reverse('project-detail', args=[project_id]))
    assert response.status_code == 200
    assert response.data['name'] == 'Test Project'
    assert response.data['owner'] == user.id

    response = client.patch(reverse('project-detail', args=[project_id]), {'description': 'Updated description'})
    assert response.status_code == 200
    assert response.data['description'] == 'Updated description'

    response = client.delete(reverse('project-detail', args=[project_id]))
    assert response.status_code == 204
    assert Project.objects.count() == 0
