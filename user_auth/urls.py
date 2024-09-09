"""
URL configuration for the `user_auth` app.

This module defines the URL patterns for handling user authentication-related
views in the `user_auth` app.

URL Patterns:
-------------
- ``''``: Maps to the `user_login` view, which handles user login.
- ``'authenticate_user'``: Maps to the `authenticate_user` view.
- ``'logout/'``: Maps to the `user_logout` view, which handles user logout.
- ``'register/'``: Maps to the `register` view, for user registration.
"""

# Libraries and modules
from django.urls import path
from . import views


app_name = 'user_auth'


urlpatterns = [
    path('', views.user_login, name='login'),
    path('authenticate_user', views.authenticate_user,
         name='authenticate_user'),
    path('logout/', views.user_logout, name='logout'),
    path('register/', views.register, name='register'),
]
