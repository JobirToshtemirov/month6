from django.contrib import admin
from django.urls import path
from auth_fur import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
]
