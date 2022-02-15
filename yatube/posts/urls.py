# posts/urls.py
from django.urls import path
from . import views

urlpatterns = [
    # Главная страница
    path('', views.index),
    #Список постов
    path(
    'group/<slug:pk>/',
    views.group_posts
    ),
    
] 