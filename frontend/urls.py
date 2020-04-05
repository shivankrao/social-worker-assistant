# frontend/urls.py

from django.urls import path

from .views import index, MainDetailView

urlpatterns = [
    path('', index),
    path('edit/<int:pk>', MainDetailView.as_view()),
    path('delete/<int:pk>', MainDetailView.as_view()),
]