from django.contrib import admin
from .models import BlogPost, Comment

@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    """
    Admin configuration for the BlogPost model.
    """
    list_display = ('title', 'author', 'timestamp', 'is_published')
    list_filter = ('is_published', 'author')
    search_fields = ('title', 'content')
    raw_id_fields = ('author',)
    date_hierarchy = 'timestamp'
    ordering = ('-timestamp',)

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    """
    Admin configuration for the Comment model.
    """
    list_display = ('user', 'blog_post', 'timestamp', 'text')
    list_filter = ('user', 'blog_post')
    search_fields = ('text',)
    date_hierarchy = 'timestamp'
    ordering = ('-timestamp',)
