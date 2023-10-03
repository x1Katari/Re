import pytest
from rest_framework.test import APIClient

client = APIClient()


@pytest.mark.django_db
def test_getList_title():
    response = client.get('/api/v1/title/')
    assert response.status_code == 200


@pytest.mark.django_db
def test_postList_title():
    response = client.post('/api/v1/title/')
    assert response.status_code == 405


@pytest.mark.django_db
def test_getDetail_title():
    response = client.get('/api/v1/title/1/')
    assert response.status_code == 200


@pytest.mark.django_db
def test_postDetail_title():
    response = client.post('/api/v1/title/1/')
    assert response.status_code == 405


@pytest.mark.django_db
def test_getList_chapter():
    response = client.get('/api/v1/chapter/')
    assert response.status_code == 200


@pytest.mark.django_db
def test_postList_chapter():
    response = client.post('/api/v1/chapter/')
    assert response.status_code == 400


@pytest.mark.django_db
def test_like_get_chapter():
    response = client.get('/api/v1/chapter/1/like/')
    assert response.status_code == 405


@pytest.mark.django_db
def test_like_post_chapter():
    response = client.post('/api/v1/chapter/1/like/')
    assert response.status_code == 200
