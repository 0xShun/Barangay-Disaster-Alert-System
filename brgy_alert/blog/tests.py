from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth import get_user_model
from .models import BlogPost, Comment

User = get_user_model()

class BlogModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser',
            email='test@example.com',
            password='testpass123'
        )
        self.blog_post = BlogPost.objects.create(
            title='Test Blog Post',
            content='This is a test blog post content.',
            author=self.user,
            is_published=True
        )

    def test_blog_post_creation(self):
        self.assertEqual(self.blog_post.title, 'Test Blog Post')
        self.assertEqual(self.blog_post.content, 'This is a test blog post content.')
        self.assertEqual(self.blog_post.author, self.user)
        self.assertTrue(self.blog_post.is_published)

    def test_blog_post_str_representation(self):
        self.assertEqual(str(self.blog_post), 'Test Blog Post')

    def test_blog_post_get_absolute_url(self):
        expected_url = reverse('blog:blog_detail', kwargs={'pk': self.blog_post.pk})
        self.assertEqual(self.blog_post.get_absolute_url(), expected_url)

    def test_comment_creation(self):
        comment = Comment.objects.create(
            blog_post=self.blog_post,
            user=self.user,
            text='This is a test comment.'
        )
        self.assertEqual(comment.blog_post, self.blog_post)
        self.assertEqual(comment.user, self.user)
        self.assertEqual(comment.text, 'This is a test comment.')

    def test_comment_str_representation(self):
        comment = Comment.objects.create(
            blog_post=self.blog_post,
            user=self.user,
            text='This is a test comment.'
        )
        expected_str = f'Comment by {self.user.username} on {self.blog_post.title}'
        self.assertEqual(str(comment), expected_str)

class BlogViewsTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(
            username='testuser',
            email='test@example.com',
            password='testpass123'
        )
        self.blog_post = BlogPost.objects.create(
            title='Test Blog Post',
            content='This is a test blog post content.',
            author=self.user,
            is_published=True
        )

    def test_blog_list_view(self):
        response = self.client.get(reverse('blog:blog_list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog/blog_list.html')
        self.assertContains(response, 'Test Blog Post')

    def test_blog_detail_view_get(self):
        response = self.client.get(reverse('blog:blog_detail', kwargs={'pk': self.blog_post.pk}))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog/blog_detail.html')
        self.assertContains(response, 'Test Blog Post')

    def test_blog_detail_view_post_comment(self):
        self.client.login(username='testuser', password='testpass123')
        response = self.client.post(reverse('blog:blog_detail', kwargs={'pk': self.blog_post.pk}), {
            'text': 'This is a test comment.'
        })
        self.assertEqual(response.status_code, 200)
        self.assertTrue(Comment.objects.filter(text='This is a test comment.').exists())

    def test_blog_detail_view_404(self):
        response = self.client.get(reverse('blog:blog_detail', kwargs={'pk': 999}))
        self.assertEqual(response.status_code, 404)
