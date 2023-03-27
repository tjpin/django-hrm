from django.contrib import admin, sites
from django.contrib.humanize.templatetags.humanize import intcomma
from django.utils.html import format_html

from .models import *
from .applications import LeaveApplication, LeaveStatus
from .attendance import Attendance
from .timesheet import Timetable
from .hrd import (Performance, Payroll, Training, Announcement)
from .models import Appointment


# //////// Actions
@admin.action(description='Conclude Leave')
def update_leave_status(modeladmin, request, queryset):
    queryset.update(status=LeaveStatus.COMPLETED)

# ////////////////////


class HRMAdminSite(admin.AdminSite):
    def get_app_list(self, request, app_label='office'):
        all_apps = super().get_app_list(request)
        return all_apps
    
    class Meta:
        site_header = "HRM"
        site_title = "HRM"

@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ['appointment', 'date', 'venue', 'status']
    list_display_links = ['date', 'appointment']
    list_filter = ['date', 'status']

@admin.register(Attendance)
class AttendanceAdmin(admin.ModelAdmin):
    list_display = ['staff', 'date', 'time_in', 'time_out', 'status']
    list_filter = ['date', 'time_in']

@admin.register(StaffShift)
class ShiftAdmin(admin.ModelAdmin):
    list_display = ['shift', 'date', 'time']


@admin.register(LeaveApplication)
class LeaveApplicationAdmin(admin.ModelAdmin):
    list_display = ['staff', 'leave_type', 'start_date', 'end_date', 'status']
    list_display_links = ['leave_type']
    actions = [update_leave_status]

@admin.register(Timetable)
class TimeTableAdmin(admin.ModelAdmin):
    list_display = ['date', 'time_in', 'time_out', 'staff', 'department']

@admin.register(Training)
class TrainingAdmin(admin.ModelAdmin):
    list_display = ['training', 'date', 'complete']

    def complete(self, obj):
        if obj.completed:
            color = "#39E711"
        else:
            color = "#ffb000"
        return format_html('<strong><p style="color: {};">{}</p></strong>'.format(color, obj.completed))

@admin.register(Performance)
class PerformanceAdmin(admin.ModelAdmin):
    list_display = ['staff', 'month', 'year']

@admin.register(Announcement)
class AnnouncementAdmin(admin.ModelAdmin):
    list_display = ['date_announced', 'sender', 'subject']
    list_display_links = ['date_announced', 'sender']

@admin.register(Payroll)
class PayrollAdmin(admin.ModelAdmin):
    list_display = ['staff', 'month', 'payment_date', 'transaction_id', 'employee_grade', 'amount_paid', 'salary_status']
    search_fields = ['staff', 'month', 'payment_date', 'transaction_id']
    list_display_links = ['staff', 'month', 'payment_date', 'transaction_id']

    def employee_grade(self, obj):
        return obj.staff.grade
    
    def amount_paid(self, obj):
        return intcomma(obj.gross_salary)
    
    def salary_status(self, obj):
        if obj.status == 'Paid':
            color = "#39E711"
        if obj.status == 'Held':
            color = "#ffb000"
        if obj.status == 'Suspended':
            color = "#f90620"

        return format_html('<strong><p style="color: {};">{}</p></strong>'.format(color, obj.status))


admin.site.register(Department)
admin.site.register(EmployeeGrade)
admin.site.register(StaffPosition)

# site = HRMAdminSite()
# admin.site = site
# sites.site = site
