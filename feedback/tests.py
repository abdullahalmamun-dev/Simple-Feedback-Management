from django.urls import reverse
from rest_framework.test import APITestCase
from .models import CustomUser, Feedback

class FeedbackAPITests(APITestCase):
    def setUp(self):
        self.user = CustomUser.objects.create_user(
            username='testuser', password='testpass', role='user')
        self.admin = CustomUser.objects.create_user(
            username='admin', password='adminpass', role='admin')

    def test_user_registration(self):
        url = reverse('register')
        data = {
            'username': 'newuser',
            'password': 'newpass123',
            'email': 'new@example.com',
            'role': 'user'
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 201)

    def test_feedback_creation(self):
        self.client.login(username='testuser', password='testpass')
        url = reverse('feedback-list')
        data = {
            'title': 'Test Feedback',
            'description': 'This is a test',
            'category': 'bug'
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 201)
