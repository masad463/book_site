from django.contrib import admin, messages
from django.contrib.auth.admin import UserAdmin
from .models import Book, Comment, Category, User


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'genre', 'category', 'status']
    list_editable = ['status']
    exclude = ['created_at']
    actions = ['make_published', 'make_draft']
    ordering = ['title', 'created_at']
    prepopulated_fields = {"slug": ("title",)}
    list_filter = ['status', 'genre', 'category']

    @admin.action(description="Опубликовать")
    def make_published(self, request, queryset):
        book = queryset.update(status="published")
        self.message_user(request, f'Было опубликованно {book} книга(и)')

    @admin.action(description="Снять с публикации")
    def make_draft(self, request, queryset):
        book = queryset.update(status="draft")
        self.message_user(request, f'Снято с публикации {book} книга(и)',
                          messages.WARNING)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('book', 'author', 'content', 'time_add')
    list_filter = ('book', 'author')
    search_fields = ('book', 'author', 'content')
    readonly_fields = ['author', 'content', 'book']


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    ordering = ['name']


admin.site.register(User, UserAdmin)
