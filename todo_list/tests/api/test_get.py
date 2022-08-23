from django.urls import reverse
from rest_framework import status as http_status

from todo_list.tests.deserialization import todo_list_response, \
    todo_item_retrieve_response, comment_response
from todo_list.tests.factories import TodoListFactory, TodoItemFactory, \
    CommentFactory

ENDPOINTS = {
    'todo_list-list': reverse('api:todo_list-list'),
    'todo_list-detail': lambda uuid: reverse('api:todo_list-detail', args=(uuid,)),
    'todo_item-detail': lambda uuid: reverse('api:todo_item-detail', args=(uuid,)),
    'comment-detail': lambda uuid: reverse('api:comment-detail', args=(uuid,))
}


class TestGetTodoListViewSet:

    def setup(self):
        TodoListFactory.create_batch(size=2)

    def test_get(self, api_client):
        todo_list = TodoListFactory(user=api_client.user)
        res = api_client.get(ENDPOINTS['todo_list-list'])
        assert res.status_code == http_status.HTTP_200_OK
        assert res.data['results'] == [todo_list_response(todo_list)]

    def test_get_detail(self, api_client):
        todo_list = TodoListFactory(user=api_client.user)
        res = api_client.get(ENDPOINTS['todo_list-detail'](todo_list.uuid))
        assert res.status_code == http_status.HTTP_200_OK
        assert res.data == todo_list_response(todo_list)


class TestGetTodoItemViewSet:

    def test_get_detail(self, api_client):
        todo_item = TodoItemFactory()
        res = api_client.get(ENDPOINTS['todo_item-detail'](todo_item.uuid))
        assert res.status_code == http_status.HTTP_200_OK
        assert res.data == todo_item_retrieve_response(todo_item)


class TestGetCommentViewSet:

    def test_get_detail(self, api_client):
        comment = CommentFactory()
        res = api_client.get(ENDPOINTS['comment-detail'](comment.uuid))
        assert res.status_code == http_status.HTTP_200_OK
        assert res.data == comment_response(comment)
