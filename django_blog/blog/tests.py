from django.test import TestCase
from django.contrib.auth.models import User
from .models import Post, Comment

class CommentTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='password')
        self.post = Post.objects.create(title='Test Post', content='Test Content')

    def test_add_comment(self):
        self.client.login(username='testuser', password='password')
        response = self.client.post(f'/posts/{self.post.id}/comments/new/', {'content': 'Test Comment'})
        self.assertEqual(Comment.objects.count(), 1)
        self.assertEqual(Comment.objects.first().content, 'Test Comment')
