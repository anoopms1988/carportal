from django.db import models
from gaadi.core.models import ExModel


class VehicleType(ExModel):
    TYPES = (
        ('car', 'Car'),
        ('bikes', 'Bikes'),
        ('trucks', 'Trucks'),
        ('other', 'Other'),
    )
    name = models.CharField(default='car', choices=TYPES, max_length=10, null=False, blank=False)

    class Meta:
        verbose_name = ("Vehicle Type")


class VehicleFormType(ExModel):
    name = models.CharField(max_length=20, null=False, blank=False)
    vehicle_type = models.ForeignKey(VehicleType, related_name='vehicle_type')

    class Meta:
        verbose_name = ("Vehicle Form Type")


class Company(ExModel):
    name = models.CharField(max_length=20, null=False, blank=False)
    vehicle_type = models.ForeignKey(VehicleType, related_name='type')
    logo = models.CharField(max_length=20, null=True, blank=True)
    description = models.TextField(null=True, blank=True)

    class Meta:
        verbose_name = ("Company")


class Dealer(ExModel):
    name = models.CharField(max_length=20, null=False, blank=False)
    city = models.CharField(max_length=20, null=False, blank=False)
    address = models.TextField(null=False, blank=False)
    phone = models.CharField(max_length=30, null=False, blank=False)
    email = models.CharField(max_length=30, null=False, blank=False)
    working_hours = models.CharField(max_length=30, null=True, blank=True)
    company = models.ForeignKey(Company, related_name='company')
    vehicle_type = models.ForeignKey(VehicleType, related_name='vehicletype')

    class Meta:
        verbose_name = ("Dealer")
