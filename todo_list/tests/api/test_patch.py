from django.urls import reverse
from faker import Faker
from rest_framework import status as http_status

from todo_list.tests.factories import TodoListFactory, TodoItemFactory, \
    CommentFactory

ENDPOINTS = {
    'todo_list-detail': lambda uuid: reverse('api:todo_list-detail', args=(uuid,)),
    'todo_item-detail': lambda uuid: reverse('api:todo_item-detail', args=(uuid,)),
    'comment-detail': lambda uuid: reverse('api:comment-detail', args=(uuid,))
}


class TestPatchTodoListViewSet:

    def setup(self):
        self.fake = Faker()

    def test_path(self, api_client):
        todo_list = TodoListFactory(user=api_client.user)
        patch_data = {'title': self.fake.name()}
        res = api_client.patch(
            ENDPOINTS['todo_list-detail'](todo_list.uuid),
            data=patch_data
        )
        assert res.status_code == http_status.HTTP_200_OK
        assert res.data['title'] == patch_data['title']
        todo_list.refresh_from_db()
        assert todo_list.title == patch_data['title']


class TestPatchTodoItemViewSet:

    def setup(self):
        self.fake = Faker()

    def test_path(self, api_client):
        todo_item = TodoItemFactory()
        patch_data = {
            'title': self.fake.name(),
            'description': self.fake.sentence()
        }
        res = api_client.patch(
            ENDPOINTS['todo_item-detail'](todo_item.uuid),
            data=patch_data
        )
        assert res.status_code == http_status.HTTP_200_OK
        assert res.data['title'] == patch_data['title']
        assert res.data['description'] == patch_data['description']
        todo_item.refresh_from_db()
        assert todo_item.title == patch_data['title']
        assert todo_item.description == patch_data['description']


class TestPatchCommentViewSet:

    def setup(self):
        self.fake = Faker()

    def test_path(self, api_client):
        comment = CommentFactory()
        patch_data = {'text': self.fake.sentence()}
        res = api_client.patch(
            ENDPOINTS['comment-detail'](comment.uuid),
            data=patch_data
        )
        assert res.status_code == http_status.HTTP_200_OK
        assert res.data['text'] == patch_data['text']
        comment.refresh_from_db()
        assert comment.text == patch_data['text']
