from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static
from auth_fur import views  

# URL Configuration

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('auth_fur/', include('auth_fur.urls', namespace="auth_fur")),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

