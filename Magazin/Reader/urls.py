from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from .views import *

urlpatterns = [
  # Burada post_list isimli bir URL tanımlanıyor
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
