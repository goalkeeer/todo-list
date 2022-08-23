import factory.fuzzy
from django.contrib.auth.models import User

from todo_list.models import TodoList, TodoItem, Comment


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    username = factory.Faker('user_name')


class TodoListFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = TodoList

    title = factory.Faker('name')
    user = factory.SubFactory(UserFactory)


class TodoItemFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = TodoItem

    title = factory.Faker('name')
    description = factory.Faker('sentence')
    list = factory.SubFactory(TodoListFactory)


class CommentFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Comment

    text = factory.Faker('sentence')
    item = factory.SubFactory(TodoItemFactory)
