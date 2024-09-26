
from django.urls import path
from car.views import home_page_view, about_page_view, booking_page_view, contact_page_view, service_page_view, \
    team_page_view, testimonial_page_view, error_page_view

urlpatterns = [

    path('about/', about_page_view),
    path('booking/', booking_page_view),
    path('contact/', contact_page_view),
    path('service/', service_page_view),
    path('team/', team_page_view),
    path('testimonial/', testimonial_page_view),
    path('error/', error_page_view),
    path('', home_page_view),
]
