"""
This module defines the URL patterns for the Django project.

It maps the root URL and additional paths to their respective URLconfs.

URL Patterns:
-------------
- ``'admin/'``: Maps to the Django admin site.
- ``''``: Includes URL patterns from the `home` app.
- ``'user_auth/'``: Includes URL patterns from the `user_auth` app.

This file serves as the central routing configuration for the project.
"""

# Libraries and modules
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    path('user_auth/', include('user_auth.urls')),
]
