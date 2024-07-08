from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import *  # Import the view

urlpatterns = [
    path('writerdashboard/<slug:slug>', writerdashboard, name='writer-dashboard'),  
    path('writer_edit/<slug:slug>', writer_edit, name='writer_edit'),  
    path('readerdashboard/', readerdashboard, name='reader-dashboard'),
    
    
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
