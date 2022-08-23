import pytest


@pytest.fixture
def api_user():
    from django.contrib.auth import get_user_model
    user_model = get_user_model()
    user = user_model(username='test', email='test@test.ru', is_active=True)
    user.set_password('test_password')
    user.save()
    return user


@pytest.fixture
def api_client(api_user):
    from rest_framework.test import APIClient
    client = APIClient()
    client.user = api_user
    client.force_login(api_user)
    return client


@pytest.fixture(autouse=True)
def enable_db_access(db):  # noqa
    pass
