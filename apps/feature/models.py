from django.db import models
from gaadi.core.models import ExModel
from django.utils.translation import ugettext_lazy as _, pgettext_lazy
from apps.vehicle.models import Variant


class ExteriorFeatures(ExModel):
    keyless_entry = models.BooleanField(default=False)
    rear_wiper = models.BooleanField(default=False)
    rear_sensing_wipers = models.BooleanField(default=False)
    alloy_wheels = models.BooleanField(default=False)
    roof_rails = models.BooleanField(default=False)
    projector_lamp = models.BooleanField(default=False)
    fog_lights = models.BooleanField(default=False)
    moon_roof = models.BooleanField(default=False)
    auto_headlamp =models.BooleanField(default=False)
    steel_rims = models.BooleanField(default=False)
    rear_spoiler = models.BooleanField(default=False)
    chrome_grill = models.BooleanField(default=False)
    daytime_running_lamp = models.BooleanField(default=False)
    variant = models.ForeignKey(Variant, related_name='exterior_features')

    class Meta:
        verbose_name = _("Exterior feature")
        verbose_name_plural = _("Exterior features")


class InteriorFeatures(ExModel):
    power_steering = models.BooleanField(default=False)
    power_windows = models.BooleanField(default=False)
    air_cond = models.BooleanField(default=False)
    anti_pinch = models.BooleanField(default=False)
    arm_rest =models.BooleanField(default=False)
    audio_system = models.BooleanField(default=False)
    bluetooth_connectivity =models.BooleanField(default=False)
    cruise_control = models.BooleanField(default=False)
    defogger = models.BooleanField(default=False)
    driver_info_display = models.BooleanField(default=False)
    driver_seat_height_adjust = models.BooleanField(default=False)
    electric_foldable_mirrors = models.BooleanField(default=False)
    electric_mirrors = models.BooleanField(default=False)
    foot_rest = models.BooleanField(default=False)
    keyless_start_stop_button =models.BooleanField(default=False)
    leather_seats = models.BooleanField(default=False)
    power_seats = models.BooleanField(default=False)
    rear_ac_vents = models.BooleanField(default=False)
    remote_boot_relese = models.BooleanField(default=False)
    reversing_camera = models.BooleanField(default=False)
    steering_controls = models.BooleanField(default=False)
    tachometer =models.BooleanField(default=False)
    variant = models.ForeignKey(Variant, related_name='interior_features')

    class Meta:
        verbose_name = _("Interior feature")
        verbose_name_plural = _("Interior features")


class SafetyFeatures(ExModel):
    abs =models.BooleanField(default=False)
    airbags = models.BooleanField(default=False)
    immobilizer =models.BooleanField(default=False)
    hill_control = models.BooleanField(default=False)
    central_locking = models.BooleanField(default=False)
    ebd = models.BooleanField(default=False)
    child_safety_lock =models.BooleanField(default=False)
    traction_control = models.BooleanField(default=False)
    hill_descent = models.BooleanField(default=False)
    esp = models.BooleanField(default=False)
    wheel_drive =models.BooleanField(default=False)
    variant = models.ForeignKey(Variant, related_name='safety_features')

    class Meta:
        verbose_name = _("Safety feature")
        verbose_name_plural = _("Safety features")
