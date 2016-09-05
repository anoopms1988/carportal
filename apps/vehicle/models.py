from django.db import models
from gaadi.core.models import ExModel
from django.utils.translation import ugettext_lazy as _, pgettext_lazy


class VehicleType(ExModel):
    TYPES = (
        ('car', 'Car'),
        ('bikes', 'Bikes'),
        ('trucks', 'Trucks'),
        ('other', 'Other'),
    )
    name = models.CharField(default='car', choices=TYPES, max_length=10, null=False, blank=False)

    class Meta:
        verbose_name = _("Vehicle Type")
        verbose_name_plural = _("Vehicle Types")


class VehicleFormType(ExModel):
    name = models.CharField(max_length=20, null=False, blank=False)
    vehicle_type = models.ForeignKey(VehicleType, related_name='vehicle_type')

    class Meta:
        verbose_name = _("Vehicle Form Type")
        verbose_name_plural = _("Vehicle Form Types")


class Company(ExModel):
    name = models.CharField(max_length=20, null=False, blank=False)
    vehicle_type = models.ForeignKey(VehicleType, related_name='type')
    logo = models.CharField(max_length=20, null=True, blank=True)
    description = models.TextField(null=True, blank=True)

    class Meta:
        verbose_name = _("Company")
        verbose_name_plural = _("Companies")


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
        verbose_name_plural = _("Dealers")


class Vehicle(ExModel):
    AVAILABILITY = (
        ('current', 'Current'),
        ('upcoming', 'Upcoming'),
        ('discontinued', 'Discontinued'),
    )
    name = models.CharField(max_length=20, null=False, blank=False)
    vehicle_form = models.ForeignKey(VehicleFormType, related_name='vehicle_form')
    vehicle_type = models.ForeignKey(VehicleType, related_name='type_of')
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


class Price(ExModel):
    showroom_price = models.CharField(max_length=20, null=False, blank=False)
    onroad_price = models.CharField(max_length=20, null=False, blank=False)
    variant = models.ForeignKey(Variant, related_name='price')
    emi = models.CharField(max_length=20, null=True, blank=True)


class Brakes(ExModel):
    rear_brakes = models.CharField(max_length=20, null=False, blank=False)
    front_brakes = models.CharField(max_length=20, null=False, blank=False)
    variant = models.ForeignKey(Variant, related_name='brakes')


class Capacity(ExModel):
    seating_capacity = models.CharField(max_length=20, null=False, blank=False)
    tank_capacity = models.CharField(max_length=20, null=False, blank=False)
    variant = models.ForeignKey(Variant, related_name='capacity')


class Dimension(ExModel):
    length = models.CharField(max_length=20, null=False, blank=False)
    width = models.CharField(max_length=20, null=False, blank=False)
    height = models.CharField(max_length=20, null=True, blank=True)
    wheelbase = models.CharField(max_length=20, null=True, blank=True)
    bootspace = models.CharField(max_length=20, null=True, blank=True)
    kerbweight = models.CharField(max_length=20, null=True, blank=True)
    variant = models.ForeignKey(Variant, related_name='dimensions')

    class Meta:
        verbose_name = ("Dimension")
        verbose_name_plural = ("Dimensions")


class Engines(ExModel):
    torque = models.CharField(max_length=20, null=False, blank=False)
    displacement = models.CharField(max_length=20, null=False, blank=False)
    power = models.CharField(max_length=20, null=False, blank=False)
    cylinders = models.CharField(max_length=20, null=False, blank=False)
    valvespercyclinder = models.CharField(max_length=20, null=False, blank=False)
    valvemechanism = models.CharField(max_length=20, null=False, blank=False)
    cyclinder_configuration = models.CharField(max_length=20, null=False, blank=False)
    variant = models.ForeignKey(Variant, related_name='engines')

    class Meta:
        verbose_name = ("Engine")
        verbose_name_plural = ("Engines")


class ExteriorFeatures(ExModel):
    keyless_entry = models.CharField(max_length=20, null=True, blank=True)
    rear_wiper = models.CharField(max_length=20, null=True, blank=True)
    rear_sensing_wipers = models.CharField(max_length=20, null=True, blank=True)
    alloy_wheels = models.CharField(max_length=20, null=True, blank=True)
    roof_rails = models.CharField(max_length=20, null=True, blank=True)
    projector_lamp = models.CharField(max_length=20, null=True, blank=True)
    fog_lights = models.CharField(max_length=20, null=True, blank=True)
    moon_roof = models.CharField(max_length=20, null=True, blank=True)
    auto_headlamp = models.CharField(max_length=20, null=True, blank=True)
    steel_rims = models.CharField(max_length=20, null=True, blank=True)
    rear_spoiler = models.CharField(max_length=20, null=True, blank=True)
    chrome_grill = models.CharField(max_length=20, null=True, blank=True)
    daytime_running_lamp = models.CharField(max_length=20, null=True, blank=True)
    variant = models.ForeignKey(Variant, related_name='exterior_features')

    class Meta:
        verbose_name = _("Exterior feature")
        verbose_name_plural = _("Exterior features")


class InteriorFeatures(ExModel):
    power_steering = models.CharField(max_length=20, null=True, blank=True)
    power_windows = models.CharField(max_length=20, null=True, blank=True)
    air_cond = models.CharField(max_length=20, null=True, blank=True)
    anti_pinch = models.CharField(max_length=20, null=True, blank=True)
    arm_rest = models.CharField(max_length=20, null=True, blank=True)
    audio_system = models.CharField(max_length=20, null=True, blank=True)
    bluetooth_connectivity = models.CharField(max_length=20, null=True, blank=True)
    cruise_control = models.CharField(max_length=20, null=True, blank=True)
    defogger = models.CharField(max_length=20, null=True, blank=True)
    driver_info_display = models.CharField(max_length=20, null=True, blank=True)
    driver_seat_height_adjust = models.CharField(max_length=20, null=True, blank=True)
    electric_foldable_mirrors = models.CharField(max_length=20, null=True, blank=True)
    electric_mirrors = models.CharField(max_length=20, null=True, blank=True)
    foot_rest = models.CharField(max_length=20, null=True, blank=True)
    keyless_start_stop_button = models.CharField(max_length=20, null=True, blank=True)
    leather_seats = models.CharField(max_length=20, null=True, blank=True)
    power_seats = models.CharField(max_length=20, null=True, blank=True)
    rear_ac_vents = models.CharField(max_length=20, null=True, blank=True)
    remote_boot_relese = models.CharField(max_length=20, null=True, blank=True)
    reversing_camera = models.CharField(max_length=20, null=True, blank=True)
    steering_controls = models.CharField(max_length=20, null=True, blank=True)
    tachometer = models.CharField(max_length=20, null=True, blank=True)

    class Meta:
        verbose_name = _("Interior feature")
        verbose_name_plural = _("Interior features")
