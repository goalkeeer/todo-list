from rest_framework.routers import DefaultRouter

from todo_list.api.viewsets import TodoListViewSet, TodoItemViewSet, \
    CommentViewSet

todo_list_router = DefaultRouter()
todo_list_router.register('todolist-list', TodoListViewSet,
                          basename='todo_list')
todo_list_router.register('todoitem-list', TodoItemViewSet,
                          basename='todo_item')
todo_list_router.register('comment-list', CommentViewSet,
                          basename='comment')
