from django.shortcuts import render
from django.shortcuts import render


def home_page_view(request):
    return render(request, 'index.html')


def about_page_view(request):
    return render(request, 'about.html')


def booking_page_view(request):
    return render(request, 'booking.html')


def contact_page_view(request):
    return render(request, 'contact.html')


def service_page_view(request):
    return render(request, 'service.html')


def team_page_view(request):
    return render(request, 'team.html')


def testimonial_page_view(request):
    return render(request, 'testimonial.html')


def error_page_view(request):
    return render(request, '404.html')
