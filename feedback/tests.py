from django.urls import reverse
from rest_framework.test import APITestCase
from .models import CustomUser, Feedback

class FeedbackTests(APITestCase):
    def setUp(self):
        self.user = CustomUser.objects.create_user(
            username='testuser', password='testpass', role='user')
        self.admin = CustomUser.objects.create_user(
            username='admin', password='adminpass', role='admin')

    def test_feedback_flow(self):
        # Login
        response = self.client.post(reverse('login'), {
            'username': 'testuser',
            'password': 'testpass'
        })
        token = response.data['access']
        
        # Create feedback
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {token}')
        response = self.client.post(reverse('feedback-list'), {
            'title': 'Test Title',
            'description': 'Test Description',
            'category': 'bug'
        })
        self.assertEqual(response.status_code, 201)
