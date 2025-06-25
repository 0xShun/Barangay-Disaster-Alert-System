from django.urls import path
from .views import BlogPostListView, BlogPostDetailView, admin_create_blog_post

app_name = 'blog'

urlpatterns = [
    path('', BlogPostListView.as_view(), name='blog_list'),
    path('<int:pk>/', BlogPostDetailView.as_view(), name='blog_detail'),
    path('admin/create/', admin_create_blog_post, name='admin_create_blog_post'),
] 