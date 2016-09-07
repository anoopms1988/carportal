from django.contrib import admin
from .models import VehicleType, VehicleFormType, Dealer, Company \
    , FuelType, RoadAssistance


# Register your models here.

class VehicleTypeAdmin(admin.ModelAdmin):
    model = VehicleType


admin.site.register(VehicleType, VehicleTypeAdmin)


class VehicleFormTypeAdmin(admin.ModelAdmin):
    model = VehicleFormType


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
