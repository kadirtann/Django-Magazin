from django.urls import path
from . import views

urlpatterns = [
    path('', views.login, name='login'),
    path('index/', views.index, name='index'),
    path('register/', views.register_view, name='register'),
    path('ana-base/', views.base, name='main/base')
    ]