from django.contrib import admin

from todo_list.models import TodoItem, Comment


class TodoItemInline(admin.TabularInline):
    model = TodoItem
    extra = 0
    show_change_link = True


class CommentInline(admin.TabularInline):
    model = Comment
    extra = 0
    show_change_link = True
