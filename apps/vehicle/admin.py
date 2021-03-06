from django.contrib import admin
from .models import VehicleFormType, Dealer, Company \
    , FuelType, RoadAssistance, Variant, Vehicle
from gaadi.core.admin_functions import activate,inactivate,archive
# Register your models here.

class VehicleFormTypeAdmin(admin.ModelAdmin):
    model = VehicleFormType
    list_display = ['name', 'vehicle_type']
    list_filter = ['status']
    search_fields = ['name']
    actions = [activate, inactivate, archive]

    activate.short_description = 'Activate selected items'
    inactivate.short_description = 'Inactivate selected items'
    archive.short_description = 'Archive selected items'


admin.site.register(VehicleFormType, VehicleFormTypeAdmin)


class DealerAdmin(admin.ModelAdmin):
    model = Dealer
    list_display = ['name', 'city', 'address', 'phone', 'email', 'working_hours', 'company', 'vehicle_type']
    list_filter = ['company', 'vehicle_type']
    search_fields = ['name']
    actions = [activate, inactivate, archive]

    activate.short_description = 'Activate selected items'
    inactivate.short_description = 'Inactivate selected items'
    archive.short_description = 'Archive selected items'


admin.site.register(Dealer, DealerAdmin)


class CompanyAdmin(admin.ModelAdmin):
    model = Company
    list_display = ['name', 'vehicle_type', 'logo', 'description']
    list_filter = ['status', 'vehicle_type']
    search_fields = ['name']
    actions = [activate, inactivate, archive]

    activate.short_description = 'Activate selected items'
    inactivate.short_description = 'Inactivate selected items'
    archive.short_description = 'Archive selected items'


admin.site.register(Company, CompanyAdmin)


class FuelTypeAdmin(admin.ModelAdmin):
    model = FuelType
    list_display = ['name']
    search_fields = ['name']


admin.site.register(FuelType, FuelTypeAdmin)


class RoadAssistanceAdmin(admin.ModelAdmin):
    model = RoadAssistance
    list_display = ['contact_details','address','phone','email','company']
    list_filter = ['status','company']
    search_fields = ['contact_details']
    actions = [activate, inactivate, archive]

    activate.short_description = 'Activate selected items'
    inactivate.short_description = 'Inactivate selected items'
    archive.short_description = 'Archive selected items'

admin.site.register(RoadAssistance, RoadAssistanceAdmin)


class VehicleAdmin(admin.ModelAdmin):
    model = Vehicle
    list_display = ['name','vehicle_form','vehicle_type','company','general_price','general_image','availability']
    list_filter = ['status','company','vehicle_type','vehicle_form','availability']
    search_fields = ['name']
    actions = [activate, inactivate, archive]

    activate.short_description = 'Activate selected items'
    inactivate.short_description = 'Inactivate selected items'
    archive.short_description = 'Archive selected items'

admin.site.register(Vehicle, VehicleAdmin)


class VariantAdmin(admin.ModelAdmin):
    model = Variant
    list_display = ['name','vehicle','fuel_type']
    list_filter=['status']
    search_fields = ['name']
    actions = [activate, inactivate, archive]

    activate.short_description = 'Activate selected items'
    inactivate.short_description = 'Inactivate selected items'
    archive.short_description = 'Archive selected items'

admin.site.register(Variant, VariantAdmin)
