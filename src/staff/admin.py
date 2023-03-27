from django.contrib import admin

from .models import *


@admin.register(Staff)
class StaffAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'staff_number', 'mobile_number', 'email', 'department', 'position', 'status']
    list_display_links = ['full_name', 'staff_number']
    radio_fields = {"gender": admin.HORIZONTAL}

@admin.register(HOD)
class HODAdmin(admin.ModelAdmin):
    list_display = ['department']

# @admin.register(StaffNextBirthday)
# class HODAdmin(admin.ModelAdmin):
#     list_display = ['full_name', 'birthday']

#     def birthday(self, obj):
        # return obj.dob.strftime("%A %d")

