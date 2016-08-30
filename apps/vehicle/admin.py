from django.contrib import admin
from .models import VehicleType, VehicleFormType, Dealer


# Register your models here.

class VehicleTypeAdmin(admin.ModelAdmin):
    model = VehicleType


class VehicleFormTypeAdmin(admin.ModelAdmin):
    model = VehicleFormType


class DealerAdmin(admin.ModelAdmin):
    model = Dealer


admin.site.register(VehicleType, VehicleTypeAdmin)
admin.site.register(VehicleFormType, VehicleFormTypeAdmin)
admin.site.register(Dealer, DealerAdmin)
