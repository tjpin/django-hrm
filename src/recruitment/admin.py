from django.contrib import admin

from .models import (Vacancy, Application, Recruit, Recruitment)

@admin.register(Recruitment)
class RecruitmentAdmin(admin.ModelAdmin):
    list_display = ['vacancy']

@admin.register(Vacancy)
class VacancyAdmin(admin.ModelAdmin):
    list_display = ['vacancy', 'number_of_vacancy']

@admin.register(Application)
class ApplicationAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'resume_name', 'position', 'date', 'email', 'mobile_number']

@admin.register(Recruit)
class RecruitAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'mobile_number', 'date', 'position', 'current_status']

    def current_status(self, obj):
        if obj.status == 'In Review':
            return "Awaiting confirmation"
        if obj.status == 'Shortlisted':
            return "Next Phase"
        if obj.status == 'Selected':
            return "Ready for On-boarding"

