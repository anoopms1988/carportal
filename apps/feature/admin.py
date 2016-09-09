from django.contrib import admin
from .models import InteriorFeatures, ExteriorFeatures, SafetyFeatures


class InteriorFeaturesAdmin(admin.ModelAdmin):
    model = InteriorFeatures
    list_display = ['get_variant_name','power_steering', 'power_windows', 'air_cond', 'anti_pinch',
                    'arm_rest', 'audio_system', 'bluetooth_connectivity', 'cruise_control',
                    'defogger', 'driver_info_display', 'driver_seat_height_adjust', 'electric_foldable_mirrors',
                    'electric_mirrors', 'foot_rest', 'keyless_start_stop_button', 'leather_seats',
                    'power_seats', 'rear_ac_vents', 'remote_boot_relese', 'reversing_camera',
                    'steering_controls', 'tachometer'
                    ]

    def get_variant_name(self, obj):
        return obj.variant.name

    get_variant_name.short_description = 'Variant'


admin.site.register(InteriorFeatures, InteriorFeaturesAdmin)


class ExteriorFeaturesAdmin(admin.ModelAdmin):
    model = ExteriorFeatures
    list_display = ['keyless_entry', 'rear_wiper', 'rear_sensing_wipers', 'alloy_wheels']


admin.site.register(ExteriorFeatures, ExteriorFeaturesAdmin)


class SafetyFeaturesAdmin(admin.ModelAdmin):
    model = SafetyFeatures
    list_display = ['abs', 'airbags', 'immobilizer', 'hill_control']


admin.site.register(SafetyFeatures, SafetyFeaturesAdmin)
