from django.urls import path
from django.contrib.auth.forms import UserCreationForm

from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('register/', views.register, name='register'),
]