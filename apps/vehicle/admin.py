from django.contrib import admin
from .models import VehicleFormType, Dealer, Company \
    , FuelType, RoadAssistance, Variant, Vehicle


# Register your models here.
class VehicleFormTypeAdmin(admin.ModelAdmin):
    model = VehicleFormType
    list_display = ['name', 'vehicle_type']
    list_filter = ['status']


admin.site.register(VehicleFormType, VehicleFormTypeAdmin)


class DealerAdmin(admin.ModelAdmin):
    model = Dealer


admin.site.register(Dealer, DealerAdmin)


class CompanyAdmin(admin.ModelAdmin):
    model = Company


admin.site.register(Company, CompanyAdmin)


class FuelTypeAdmin(admin.ModelAdmin):
    model = FuelType


admin.site.register(FuelType, FuelTypeAdmin)


class RoadAssistanceAdmin(admin.ModelAdmin):
    model = RoadAssistance


admin.site.register(RoadAssistance, RoadAssistanceAdmin)


class VehicleAdmin(admin.ModelAdmin):
    model = Vehicle


admin.site.register(Vehicle, VehicleAdmin)


class VariantAdmin(admin.ModelAdmin):
    model = Variant


admin.site.register(Variant, VariantAdmin)
