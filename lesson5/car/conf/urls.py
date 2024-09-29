from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from car.views import book_info_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('form/', include, book_info_view, name='form'),
    path('', include('services.urls')),

]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_rooy=settings.MEDIA_ROOT)
