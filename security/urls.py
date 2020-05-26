from django.contrib import admin
from django.urls import path, include, re_path

from security import views

namespace = 'security'

urlpatterns = [
    path('register/', views.RegisterView.as_view(), name='register'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('logout/', views.logout_func, name='logout'),
]
