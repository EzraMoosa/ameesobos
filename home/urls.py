# Libraries and modules
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views


app_name = 'home'


urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('members/', views.members_list, name='members'),
    path('songs/', views.songs_list, name='songs'),
    path('songs/<int:pk>/', views.song_detail, name='song_detail'),
    path('events/', views.events_list, name='events'),
 ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) # 1 - 2

# Research & Resources
# 1. https://docs.djangoproject.com/en/2.1/howto/static-files/#serving-files-uploaded-by-a-user-during-development
# 2. https://stackoverflow.com/questions/5517950/django-media-url-and-media-root
