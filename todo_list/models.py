import uuid

from django.contrib.auth import get_user_model
from django.db import models


def _new_uuid():
    return uuid.uuid4()


class PrimaryUuid(models.Model):
    uuid = models.UUIDField(
        primary_key=True, default=_new_uuid, editable=False
    )

    def __str__(self):
        return str(self.uuid)

    class Meta:
        abstract = True


class Dated(models.Model):
    created = models.DateTimeField(
        editable=False,
        auto_now_add=True,
        db_index=True,
    )
    updated = models.DateTimeField(
        editable=False,
        auto_now=True,
        db_index=True,
    )

    class Meta:
        abstract = True


class TodoList(PrimaryUuid, Dated):
    title = models.CharField(max_length=256, db_index=True)
    user = models.ForeignKey(to=get_user_model(), on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        default_related_name = 'lists'
        unique_together = [('user', 'title')]
        ordering = ['created']


class TodoItem(PrimaryUuid, Dated):
    title = models.CharField(max_length=256, db_index=True)
    description = models.TextField(default='', blank=True)
    list = models.ForeignKey(to=TodoList, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        default_related_name = 'items'
        unique_together = [('list', 'title')]
        ordering = ['created']


class Comment(PrimaryUuid, Dated):
    text = models.TextField()
    item = models.ForeignKey(to=TodoItem, on_delete=models.CASCADE)

    class Meta:
        default_related_name = 'comments'
        ordering = ['-created']
