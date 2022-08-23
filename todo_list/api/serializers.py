from rest_framework import serializers

from todo_list.models import TodoList, Comment, TodoItem


class CommentSerializer(serializers.ModelSerializer):
    item_id = serializers.PrimaryKeyRelatedField(
        write_only=True,
        queryset=TodoItem.objects.all(),
        source='item',
    )

    class Meta:
        model = Comment
        fields = ('uuid', 'text', 'created', 'updated', 'item_id')
        read_only_field = ('uuid', 'created', 'updated')


class TodoItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = TodoItem
        fields = ('uuid', 'title', 'description', 'created', 'updated')
        read_only_field = ('uuid', 'created', 'updated')


class TodoItemSerializerRetrieve(TodoItemSerializer):
    comments = CommentSerializer(many=True, required=False, read_only=True)
    list_id = serializers.PrimaryKeyRelatedField(
        write_only=True,
        queryset=TodoList.objects.all(),
        source='list'
    )

    class Meta:
        model = TodoItem
        fields = TodoItemSerializer.Meta.fields + ('comments', 'list_id')
        read_only_field = TodoItemSerializer.Meta.read_only_field


class TodoListSerializer(serializers.ModelSerializer):
    items = TodoItemSerializer(many=True, required=False)

    class Meta:
        model = TodoList
        fields = ('uuid', 'title', 'created', 'updated', 'items')
        read_only_field = ('uuid', 'created', 'updated')

    def create(self, validated_data):
        user = self.context['request'].user
        validated_data['user'] = user
        items = validated_data.pop('items', [])
        instance = super().create(validated_data)
        for item in items:
            TodoItem.objects.create(list=instance, **item)
        return instance
