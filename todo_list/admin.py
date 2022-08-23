from django.contrib import admin

from todo_list.admin_site.admin import TodoListAdmin, TodoItemAdmin, \
    CommentAdmin
from todo_list.models import TodoList, TodoItem, Comment

admin.site.register(TodoList, TodoListAdmin)
admin.site.register(TodoItem, TodoItemAdmin)
admin.site.register(Comment, CommentAdmin)
