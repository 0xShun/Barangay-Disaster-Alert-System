from django.db import models
from django.conf import settings
from django.urls import reverse

class BlogPost(models.Model):
    """
    Represents a blog post with a title, content, author, and publication status.
    """
    title = models.CharField(max_length=200)
    content = models.TextField()
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='blog_posts')
    timestamp = models.DateTimeField(auto_now_add=True)
    is_published = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:blog_detail', kwargs={'pk': self.pk})

    class Meta:
        ordering = ['-timestamp']

class Comment(models.Model):
    """
    Represents a comment made by a user on a specific blog post.
    """
    blog_post = models.ForeignKey(BlogPost, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='comments')
    text = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Comment by {self.user.username} on {self.blog_post.title}'

    class Meta:
        ordering = ['timestamp']
