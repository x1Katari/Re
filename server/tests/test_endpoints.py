import pytest
from rest_framework.test import APIClient

client = APIClient()


@pytest.mark.django_db
def test_getList():
    response = client.get('/api/v1/title/')
    assert response.status_code == 200


@pytest.mark.django_db
def test_postList():
    response = client.post('/api/v1/title/')
    assert response.status_code == 405


@pytest.mark.django_db
def test_getDetail():
    response = client.get('/api/v1/title/1/')
    assert response.status_code == 200


@pytest.mark.django_db
def test_postDetail():
    response = client.post('/api/v1/title/1/')
    assert response.status_code == 405


@pytest.mark.django_db
def test_like_get():
    response = client.get('/api/v1/title/1/like/')
    assert response.status_code == 405


@pytest.mark.django_db
def test_like_post():
    response = client.post('/api/v1/title/1/like/')
    assert response.status_code == 200
