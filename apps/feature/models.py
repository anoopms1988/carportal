from django.db import models
from gaadi.core.models import ExModel
from django.utils.translation import ugettext_lazy as _, pgettext_lazy
from apps.vehicle.models import Variant


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
    variant = models.ForeignKey(Variant, related_name='interior_features')

    class Meta:
        verbose_name = _("Interior feature")
        verbose_name_plural = _("Interior features")


class SafetyFeatures(ExModel):
    abs = models.CharField(max_length=20, null=True, blank=True)
    airbags = models.CharField(max_length=20, null=True, blank=True)
    immobilizer = models.CharField(max_length=20, null=True, blank=True)
    hill_control = models.CharField(max_length=20, null=True, blank=True)
    central_locking = models.CharField(max_length=20, null=True, blank=True)
    ebd = models.CharField(max_length=20, null=True, blank=True)
    child_safety_lock = models.CharField(max_length=20, null=True, blank=True)
    traction_control = models.CharField(max_length=20, null=True, blank=True)
    hill_descent = models.CharField(max_length=20, null=True, blank=True)
    esp = models.CharField(max_length=20, null=True, blank=True)
    wheel_drive = models.CharField(max_length=20, null=True, blank=True)
    variant = models.ForeignKey(Variant, related_name='safety_features')

    class Meta:
        verbose_name = _("Safety feature")
        verbose_name_plural = _("Safety features")
