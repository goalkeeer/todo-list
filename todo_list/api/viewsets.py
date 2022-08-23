from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter
from rest_framework.mixins import RetrieveModelMixin, ListModelMixin, \
    CreateModelMixin, UpdateModelMixin
from rest_framework.viewsets import GenericViewSet

from todo_list.api.filters import TodoListFilter
from todo_list.api.serializers import TodoListSerializer, \
    TodoItemSerializerRetrieve, CommentSerializer
from todo_list.models import TodoList, TodoItem, Comment


class TodoListViewSet(
    RetrieveModelMixin,
    ListModelMixin,
    CreateModelMixin,
    UpdateModelMixin,
    GenericViewSet,
):

    queryset = TodoList.objects.all()
    serializer_class = TodoListSerializer
    filter_backends = (OrderingFilter, DjangoFilterBackend)
    filterset_class = TodoListFilter
    ordering_fields = ('created', 'updated', 'title')

    def get_queryset(self):
        user = self.request.user
        queryset = super().get_queryset()
        queryset = queryset.prefetch_related('items')
        return queryset.filter(user=user)


class TodoItemViewSet(
    RetrieveModelMixin,
    CreateModelMixin,
    UpdateModelMixin,
    GenericViewSet,
):

    queryset = TodoItem.objects.all()
    serializer_class = TodoItemSerializerRetrieve

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.prefetch_related('comments')


class CommentViewSet(
    RetrieveModelMixin,
    CreateModelMixin,
    UpdateModelMixin,
    GenericViewSet,
):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
