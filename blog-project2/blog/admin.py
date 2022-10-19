from django.contrib import admin
from .models import Post, Comment, Category


# Register your models here.
#admin.site.register(Post)

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "status", "created", "publish", "author")
    prepopulated_fields = {'slug':("title",)}
    search_fields = ('title',)
    ordering = ("author", "status")
    list_filter = ("author", "created", "publish")

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}

admin.site.register(Category, CategoryAdmin)

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'created')
    search_fields = ('username',)
