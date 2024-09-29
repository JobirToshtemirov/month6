from django.urls import path
from . import views

urlpatterns = [
    path('', views.book_list_view, name='book_list'),
    path('add/', views.book_add_view, name='book_add'),
    path('edit/<int:book_id>/', views.book_edit_view, name='book_edit'),
    path('delete/<int:book_id>/', views.book_delete_view, name='book_delete'),
]
