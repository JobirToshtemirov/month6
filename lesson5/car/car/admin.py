from django.contrib import admin

# Register your models here.

from django.contrib import admin

from .models import CustomerModel, CarModel, ServiceModel

admin.site.register(CustomerModel)
admin.site.register(CarModel)
admin.site.register(ServiceModel)
