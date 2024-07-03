from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('Reader.urls')),  # Root URL handled by Reader app
    path('login/', include('Login.urls')),
    path('writer/', include('Writer.urls')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
