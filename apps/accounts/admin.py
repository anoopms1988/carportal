from django.contrib import admin
from .models import UserProfile


# Register your models here.

class UserProfileAdmin(admin.ModelAdmin):
    model = UserProfile
    list_display = ['first_name', 'last_name', 'email', 'gender', 'city', 'mobile', 'address']

    def first_name(self, obj):
        return obj.user.first_name

    def last_name(self, obj):
        return obj.user.last_name

    def email(self, obj):
        return obj.user.email

    first_name.short_description = 'First name'
    last_name.short_description = 'Last name'
    email.short_description = 'Email'


admin.site.register(UserProfile, UserProfileAdmin)
