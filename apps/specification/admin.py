from django.contrib import admin
from .models import Steering, Brakes, Price, Dimension, Engines, Wheel, Capacity


# Register your models here.
class SteeringAdmin(admin.ModelAdmin):
    model = Steering
    list_display = ['turning_radius', 'steering_type']


admin.site.register(Steering, SteeringAdmin)


class PriceAdmin(admin.ModelAdmin):
    model = Price
    list_display = ['showroom_price', 'onroad_price', 'emi']


admin.site.register(Price, PriceAdmin)


class BrakesAdmin(admin.ModelAdmin):
    model = Brakes
    list_display = ['rear_brakes', 'front_brakes']


admin.site.register(Brakes, BrakesAdmin)

class CapacityAdmin(admin.ModelAdmin):
    model = Capacity
    list_display = ['seating_capacity', 'tank_capacity']

admin.site.register(Capacity, CapacityAdmin)

class DimensionAdmin(admin.ModelAdmin):
    model = Dimension
    list_display = ['length', 'width','height','wheelbase','bootspace','kerbweight']

admin.site.register(Dimension, DimensionAdmin)

class EnginesAdmin(admin.ModelAdmin):
    model = Engines
    list_display = ['torque', 'displacement','power','cylinders','valvespercyclinder',
                    'valvemechanism','cyclinder_configuration']

admin.site.register(Engines, EnginesAdmin)

class WheelAdmin(admin.ModelAdmin):
    model = Wheel
    list_display = ['wheel_size', 'wheel_type','variant']

admin.site.register(Wheel, WheelAdmin)