from django.db import models
from gaadi.core.models import ExModel
from django.utils.translation import ugettext_lazy as _, pgettext_lazy
from apps.vehicle.models import Variant


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
        verbose_name = _("Dimension")
        verbose_name_plural = _("Dimensions")


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
        verbose_name = _("Engine")
        verbose_name_plural = _("Engines")


class Steering(ExModel):
    turning_radius = models.CharField(max_length=20, null=False, blank=False)
    steering_type = models.CharField(max_length=20, null=False, blank=False)
    variant = models.ForeignKey(Variant, related_name='steering')

    class Meta:
        verbose_name = _("Steering")
        verbose_name_plural = _("Steering")


class Wheel(ExModel):
    wheel_size = models.CharField(max_length=20, null=False, blank=False)
    wheel_type = models.CharField(max_length=20, null=False, blank=False)
    variant = models.ForeignKey(Variant, related_name='wheel')

    class Meta:
        verbose_name = _("Wheel")
        verbose_name_plural = _("Wheel")


