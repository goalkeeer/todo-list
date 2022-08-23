import pytest

from todo_list.models import TodoList, TodoItem, Comment
from todo_list.tests.factories import TodoListFactory, TodoItemFactory, \
    CommentFactory


@pytest.fixture(params=[
    (TodoList, TodoListFactory),
    (TodoItem, TodoItemFactory),
    (Comment, CommentFactory),
])
def model_and_factory(request):
    return request.param


@pytest.mark.django_db
def test_create_model_by_factory(model_and_factory):
    model, factory = model_and_factory
    obj1 = factory.create()
    obj2 = model.objects.last()
    assert obj1.uuid == obj2.uuid
    assert str(obj1) == str(obj2)
