from django.db import models
from django.db import models


class CustomerModel(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=15)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Customer'
        verbose_name_plural = 'Customers'


class CarModel(models.Model):
    make = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    year = models.IntegerField()
    customer = models.ForeignKey(CustomerModel, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.make} {self.model} ({self.year})"

    class Meta:
        verbose_name = 'Car'
        verbose_name_plural = 'Cars'


class ServiceModel(models.Model):
    CAR_SERVICE_TYPES = (
        ('w', 'Wash'),
        ('c', 'Clean'),
        ('o', 'Oil Change'),
        ('b', 'Brake Service'),
        ('g', 'Glass Cleaning'),
        ('e', 'Engine Service'),
        ('r', 'Radiator Service'),
        ('o', 'Other'))
    car = models.ForeignKey(CarModel, on_delete=models.CASCADE)
    service_type = models.CharField(max_length=1, choices=CAR_SERVICE_TYPES)
    description = models.TextField()
    date = models.DateField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.car.make} {self.car.model} ({self.car.year}) - {self.get_service_type_display()}"

    class Meta:
        verbose_name = 'Service'
        verbose_name_plural = 'Services'
