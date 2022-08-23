from django_filters import rest_framework

from todo_list.models import TodoList


class TodoListFilter(rest_framework.FilterSet):

    class Meta:
        model = TodoList
        fields = {
            'updated': ['gt', 'lt', 'gte', 'lte'],
            'created': ['gt', 'lt', 'gte', 'lte'],
        }
