from django.urls import reverse
from faker import Faker
from rest_framework import status as http_status

from todo_list.models import TodoList, TodoItem, Comment
from todo_list.tests.deserialization import todo_list_response
from todo_list.tests.factories import TodoListFactory, TodoItemFactory

ENDPOINTS = {
    'todo_list-list': reverse('api:todo_list-list'),
    'todo_item-list': reverse('api:todo_item-list'),
    'comment-list': reverse('api:comment-list'),
}


class TestPostTodoListViewSet:

    def setup(self):
        self.fake = Faker()

    def test_post(self, api_client):
        post_data = {'title': self.fake.name()}
        res = api_client.post(
            ENDPOINTS['todo_list-list'],
            data=post_data,
            format='json'
        )
        assert res.status_code == http_status.HTTP_201_CREATED
        assert res.data['title'] == post_data['title']
        assert res.data == todo_list_response(TodoList.objects.first())

    def test_post_with_items(self, api_client):
        post_data = {
            'title': self.fake.name(),
            'items': [{
                'title': self.fake.name(),
                'description': self.fake.sentence()
            }]
        }
        res = api_client.post(
            ENDPOINTS['todo_list-list'],
            data=post_data,
            format='json'
        )
        assert res.status_code == http_status.HTTP_201_CREATED
        assert res.data['title'] == post_data['title']
        item = res.data['items'][0]
        assert item['title'] == post_data['items'][0]['title']
        assert item['description'] == post_data['items'][0]['description']


class TestPostTodoItemViewSet:

    def setup(self):
        self.fake = Faker()

    def test_post(self, api_client):
        todo_list = TodoListFactory()
        post_data = {
            'title': self.fake.name(),
            'description': self.fake.sentence(),
            'list_id': todo_list.uuid
        }
        res = api_client.post(
            ENDPOINTS['todo_item-list'],
            data=post_data,
            format='json'
        )
        assert res.status_code == http_status.HTTP_201_CREATED
        assert res.data['title'] == post_data['title']
        assert res.data['description'] == post_data['description']
        todo_item = TodoItem.objects.get(uuid=res.data['uuid'])
        assert todo_item.list == todo_list


class TestPostCommentViewSet:

    def setup(self):
        self.fake = Faker()

    def test_post(self, api_client):
        todo_item = TodoItemFactory()
        post_data = {
            'text': self.fake.sentence(),
            'item_id': todo_item.uuid
        }
        res = api_client.post(
            ENDPOINTS['comment-list'],
            data=post_data,
            format='json'
        )
        assert res.status_code == http_status.HTTP_201_CREATED
        assert res.data['text'] == post_data['text']
        comment = Comment.objects.get(uuid=res.data['uuid'])
        assert comment.item == todo_item
