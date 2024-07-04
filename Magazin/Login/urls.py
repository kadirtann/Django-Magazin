from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login, name="login"),
    path('register/', views.register_view, name='register'),
    path('main/base/', views.base, name='base'),
    path('', views.index, name='index'),
]
