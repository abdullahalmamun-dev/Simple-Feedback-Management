from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    ROLES = (
        ('user', 'User'),
        ('admin', 'Admin'),
    )
    role = models.CharField(max_length=20, choices=ROLES, default='user')

class Feedback(models.Model):
    CATEGORIES = (
        ('bug', 'Bug Report'),
        ('feature', 'Feature Request'), 
        ('general', 'General Feedback'),
    )
    STATUSES = (
        ('pending', 'Pending'),
        ('resolved', 'Resolved'),
    )
    
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField()
    category = models.CharField(max_length=20, choices=CATEGORIES)
    status = models.CharField(max_length=20, choices=STATUSES, default='pending')
    created_at = models.DateTimeField(auto_now_add=True)
