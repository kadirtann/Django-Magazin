from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
<<<<<<< HEAD
    path('reader/', include('Reader.urls')),  
    path('login/', include('Login.urls')),
    path('writer/', include('Writer.urls')),
    path('dashboard/', include('Dashboard.urls')),
    path('',include('Main.urls'))
] 

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
=======
    path('login/', include('Login.urls')),
    path('writer/', include('Writer.urls')),
    # Diğer URL yönlendirmeleri
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
>>>>>>> 1d8751b32b848d62d38b9f37978c5b742c64354b
