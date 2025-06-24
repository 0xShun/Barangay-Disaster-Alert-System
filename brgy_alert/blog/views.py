from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from django.views import View
from .models import BlogPost, Comment
from .forms import CommentForm

# Create your views here.

class BlogPostListView(ListView):
    """
    Displays a list of all published blog posts.
    """
    model = BlogPost
    template_name = 'blog/blog_list.html'
    context_object_name = 'posts'
    queryset = BlogPost.objects.filter(is_published=True)

class BlogPostDetailView(View):
    """
    Displays a single blog post and handles comment submissions.
    """
    def get(self, request, *args, **kwargs):
        post = get_object_or_404(BlogPost, pk=kwargs['pk'])
        comment_form = CommentForm()
        return render(request, 'blog/blog_detail.html', {'post': post, 'comment_form': comment_form})

    def post(self, request, *args, **kwargs):
        post = get_object_or_404(BlogPost, pk=kwargs['pk'])
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.blog_post = post
            new_comment.user = request.user
            new_comment.save()
            comment_form = CommentForm() # Reset form
        
        return render(request, 'blog/blog_detail.html', {'post': post, 'comment_form': comment_form})
