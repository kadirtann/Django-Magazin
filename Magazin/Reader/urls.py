from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from .views import *

urlpatterns = [
    path('', base, name='Reader/base.html'),  # Root URL handled by Reader app
   
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
