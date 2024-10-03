from django.urls import path
from . import views

app_name = 'auth_fur'

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('verify-email/<uidb64>/token', views.register, name='email'),

]