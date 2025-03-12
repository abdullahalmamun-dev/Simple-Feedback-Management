from django.urls import path
from .views import (
    RegisterView,
    CustomTokenObtainPairView,
    FeedbackListCreateView,
    FeedbackDetailView
)

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', CustomTokenObtainPairView.as_view(), name='login'),
    path('feedback/', FeedbackListCreateView.as_view(), name='feedback-list'),
    path('feedback/<int:pk>/', FeedbackDetailView.as_view(), name='feedback-detail'),
]
