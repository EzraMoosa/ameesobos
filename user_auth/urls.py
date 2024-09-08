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
