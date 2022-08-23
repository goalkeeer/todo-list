from django.contrib import admin

from todo_list.admin_site.inline_admin import TodoItemInline, CommentInline


class TodoListAdmin(admin.ModelAdmin):
    list_display = ('uuid', 'title', 'user')
    fieldsets = (
        (
            None,
            {'fields': ['title', 'user']}
        ),
        (
            'meta',
            {'classes': ('collapse', ),
             'fields': ['uuid', 'created', 'updated']}
        )
    )
    readonly_fields = ('created', 'updated', 'uuid')
    search_fields = ('uid', 'title', 'user__username')
    inlines = [TodoItemInline]


class TodoItemAdmin(admin.ModelAdmin):
    list_display = ('uuid', 'title', 'list')
    fieldsets = (
        (
            None,
            {'fields': ['title', 'list', 'description']}
        ),
        (
            'meta',
            {'classes': ('collapse', ),
             'fields': ['uuid', 'created', 'updated']}
        )
    )
    readonly_fields = ('created', 'updated', 'uuid')
    search_fields = ('uid', 'title', 'list__title')
    inlines = [CommentInline]


class CommentAdmin(admin.ModelAdmin):
    list_display = ('uuid', 'text', 'item')
    fieldsets = (
        (
            None,
            {'fields': ['text', 'item']}
        ),
        (
            'meta',
            {'classes': ('collapse', ),
             'fields': ['uuid', 'created', 'updated']}
        )
    )
    readonly_fields = ('created', 'updated', 'uuid')
    search_fields = ('uid', 'text', 'item__title')
