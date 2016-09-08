from django.db import models
from gaadi.core.models import ExModel
from django.utils.translation import ugettext_lazy as _, pgettext_lazy


class VehicleFormType(ExModel):
    TYPES = (
        ('car', 'Car'),
        ('bikes', 'Bikes'),
        ('trucks', 'Trucks'),
        ('other', 'Other'),
    )
    name = models.CharField(max_length=20, null=False, blank=False)
    vehicle_type = models.CharField(default='car', choices=TYPES, max_length=10, null=False, blank=False)

    class Meta:
        verbose_name = _("Vehicle Form Type")
        verbose_name_plural = _("Vehicle Form Types")


class Company(ExModel):
    TYPES = (
        ('car', 'Car'),
        ('bikes', 'Bikes'),
        ('trucks', 'Trucks'),
        ('other', 'Other'),
    )
    name = models.CharField(max_length=20, null=False, blank=False)
    vehicle_type = models.CharField(default='car', choices=TYPES, max_length=10, null=False, blank=False)
    logo = models.CharField(max_length=20, null=True, blank=True)
    description = models.TextField(null=True, blank=True)

    class Meta:
        verbose_name = _("Company")
        verbose_name_plural = _("Companies")


class Dealer(ExModel):
    TYPES = (
        ('car', 'Car'),
        ('bikes', 'Bikes'),
        ('trucks', 'Trucks'),
        ('other', 'Other'),
    )
    name = models.CharField(max_length=20, null=False, blank=False)
    city = models.CharField(max_length=20, null=False, blank=False)
    address = models.TextField(null=False, blank=False)
    phone = models.CharField(max_length=30, null=False, blank=False)
    email = models.CharField(max_length=30, null=False, blank=False)
    working_hours = models.CharField(max_length=30, null=True, blank=True)
    company = models.ForeignKey(Company, related_name='company')
    vehicle_type = models.CharField(default='car', choices=TYPES, max_length=10, null=False, blank=False)

    class Meta:
        verbose_name = ("Dealer")
        verbose_name_plural = _("Dealers")


class Vehicle(ExModel):
    AVAILABILITY = (
        ('current', 'Current'),
        ('upcoming', 'Upcoming'),
        ('discontinued', 'Discontinued'),
    )
    TYPES = (
        ('car', 'Car'),
        ('bikes', 'Bikes'),
        ('trucks', 'Trucks'),
        ('other', 'Other'),
    )
    name = models.CharField(max_length=20, null=False, blank=False)
    vehicle_form = models.ForeignKey(VehicleFormType, related_name='vehicle_form')
    vehicle_type = models.CharField(default='car', choices=TYPES, max_length=10, null=False, blank=False)
    company = models.ForeignKey(Company, related_name='company_of')
    general_price = models.CharField(max_length=20, null=True, blank=True)
    general_image = models.CharField(max_length=20, null=True, blank=True)
    availability = models.CharField(default='current', choices=AVAILABILITY, max_length=20, null=False, blank=False)

    class Meta:
        verbose_name = _("Vehicle")
        verbose_name_plural = _("Vehicles")


class FuelType(models.Model):
    name = models.CharField(max_length=20, null=False, blank=False)


class Variant(ExModel):
    name = models.CharField(max_length=20, null=False, blank=False)
    vehicle = models.ForeignKey(Vehicle, related_name='vehicle')
    fuel_type = models.ForeignKey(FuelType, related_name='fuel_type')


class RoadAssistance(ExModel):
    contact_details = models.CharField(max_length=20, null=False, blank=False)
    address = models.CharField(max_length=20, null=False, blank=False)
    phone = models.CharField(max_length=30, null=False, blank=False)
    email = models.CharField(max_length=30, null=False, blank=False)
    company = models.ForeignKey(Company, related_name='road_assistance')

    class Meta:
        verbose_name = _("Road assistance")
        verbose_name_plural = _("Road assistance")
