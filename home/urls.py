# Libraries and modules
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

"""
This module defines URL patterns for the `home` app in the Django project.

It maps URL paths to view functions and handles media files during
development.

URL Patterns:
-------------
- ``'/'``: Maps to `homepage` view function.
- ``'members/'``: Maps to `members_list` view function.
- ``'songs/'``: Maps to `songs_list` view function.
- ``'songs/<int:pk>/'``: Maps to `song_detail` view function, where
  `<int:pk>` is the primary key of the song.
- ``'events/'``: Maps to `events_list` view function.
"""


app_name = 'home'


urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('members/', views.members_list, name='members'),
    path('songs/', views.songs_list, name='songs'),
    path('songs/<int:pk>/', views.song_detail, name='song_detail'),
    path('events/', views.events_list, name='events'),
 ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)  # 1 - 2

# Research & Resources
# 1. https://docs.djangoproject.com/en/2.1/howto/static-files/#serving-files-uploaded-by-a-user-during-development
# 2. https://stackoverflow.com/questions/5517950/django-media-url-and-media-root
