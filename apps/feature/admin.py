from django.contrib import admin
from .models import InteriorFeatures,ExteriorFeatures,SafetyFeatures

class InteriorFeaturesAdmin(admin.ModelAdmin):
    model =InteriorFeatures
    list_display = ['power_steering', 'power_windows', 'air_cond', 'anti_pinch']

admin.site.register(InteriorFeatures, InteriorFeaturesAdmin)

class ExteriorFeaturesAdmin(admin.ModelAdmin):
    model =ExteriorFeatures
    list_display = ['keyless_entry', 'rear_wiper', 'rear_sensing_wipers', 'alloy_wheels']

admin.site.register(ExteriorFeatures,ExteriorFeaturesAdmin)

class SafetyFeaturesAdmin(admin.ModelAdmin):
    model =SafetyFeatures
    list_display=['abs', 'airbags', 'immobilizer', 'hill_control']

admin.site.register(SafetyFeatures,SafetyFeaturesAdmin)

