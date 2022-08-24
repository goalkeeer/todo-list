from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework import status as http_status
from faker import Faker


def test_register_user(anon_api_client):
    fake = Faker()
    post_data = {
        'username': fake.user_name(),
        'password': fake.md5(),
    }
    post_data['password2'] = post_data['password']

    url = reverse('auth:register')
    res = anon_api_client.post(url, data=post_data)
    assert res.status_code == http_status.HTTP_201_CREATED
    user = User.objects.get()
    assert user.username == post_data['username']
