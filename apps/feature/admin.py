from django.contrib import admin
from .models import InteriorFeatures, ExteriorFeatures, SafetyFeatures
from gaadi.core.admin_functions import activate,inactivate,archive


class InteriorFeaturesAdmin(admin.ModelAdmin):
    model = InteriorFeatures
    list_display = ['get_variant_name', 'get_vehicle', 'power_steering', 'power_windows', 'air_cond', 'anti_pinch',
                    'arm_rest', 'audio_system', 'bluetooth_connectivity', 'cruise_control',
                    'defogger', 'driver_info_display', 'driver_seat_height_adjust', 'electric_foldable_mirrors',
                    'electric_mirrors', 'foot_rest', 'keyless_start_stop_button', 'leather_seats',
                    'power_seats', 'rear_ac_vents', 'remote_boot_relese', 'reversing_camera',
                    'steering_controls', 'tachometer'
                    ]
    actions = [activate, inactivate, archive]

    activate.short_description = 'Activate selected items'
    inactivate.short_description = 'Inactivate selected items'
    archive.short_description = 'Archive selected items'


    def get_variant_name(self, obj):
        return obj.variant.name

    def get_vehicle(self, obj):
        return obj.variant.vehicle.name

    get_variant_name.short_description = 'Variant'
    get_vehicle.short_description = 'Vehicle'


admin.site.register(InteriorFeatures, InteriorFeaturesAdmin)


class ExteriorFeaturesAdmin(admin.ModelAdmin):
    model = ExteriorFeatures
    list_display = ['get_variant_name','get_vehicle','keyless_entry', 'rear_wiper', 'rear_sensing_wipers', 'alloy_wheels','roof_rails',
                    'projector_lamp','fog_lights','moon_roof','auto_headlamp','steel_rims','rear_spoiler',
                    'chrome_grill','daytime_running_lamp'
                    ]
    actions = [activate, inactivate, archive]

    activate.short_description = 'Activate selected items'
    inactivate.short_description = 'Inactivate selected items'
    archive.short_description = 'Archive selected items'

    def get_variant_name(self, obj):
        return obj.variant.name

    def get_vehicle(self, obj):
        return obj.variant.vehicle.name

    get_variant_name.short_description = 'Variant'
    get_vehicle.short_description = 'Vehicle'


admin.site.register(ExteriorFeatures, ExteriorFeaturesAdmin)


class SafetyFeaturesAdmin(admin.ModelAdmin):
    model = SafetyFeatures
    list_display = ['get_variant_name','get_vehicle','abs', 'airbags', 'immobilizer', 'hill_control',
                    'central_locking','ebd','child_safety_lock','traction_control',
                    'hill_descent','esp','wheel_drive'
                    ]
    actions = [activate, inactivate, archive]

    activate.short_description = 'Activate selected items'
    inactivate.short_description = 'Inactivate selected items'
    archive.short_description = 'Archive selected items'

    def get_variant_name(self, obj):
        return obj.variant.name

    def get_vehicle(self, obj):
        return obj.variant.vehicle.name

    get_variant_name.short_description = 'Variant'
    get_vehicle.short_description = 'Vehicle'

admin.site.register(SafetyFeatures, SafetyFeaturesAdmin)
