from collections import OrderedDict

from todo_list.models import Comment, TodoItem, TodoList


def comment_response(comment: Comment) -> OrderedDict:
    return OrderedDict([
        ('uuid', str(comment.uuid)),
        ('text', comment.text),
        ('created', comment.created.isoformat()),
        ('updated', comment.updated.isoformat()),
    ])


def todo_item_response(todo_item: TodoItem) -> OrderedDict:
    return OrderedDict([
        ('uuid', str(todo_item.uuid)),
        ('title', todo_item.title),
        ('description', todo_item.description),
        ('created', todo_item.created.isoformat()),
        ('updated', todo_item.updated.isoformat()),
    ])


def todo_item_retrieve_response(todo_item: TodoItem) -> OrderedDict:
    return OrderedDict([
        ('uuid', str(todo_item.uuid)),
        ('title', todo_item.title),
        ('description', todo_item.description),
        ('created', todo_item.created.isoformat()),
        ('updated', todo_item.updated.isoformat()),
        ('comments', [comment_response(c) for c in todo_item.comments.all()])
    ])


def todo_list_response(todo_list: TodoList) -> OrderedDict:
    return OrderedDict([
        ('uuid', str(todo_list.uuid)),
        ('title', todo_list.title),
        ('created', todo_list.created.isoformat()),
        ('updated', todo_list.updated.isoformat()),
        ('items', [todo_item_response(i) for i in todo_list.items.all()])
    ])
