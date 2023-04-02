from django.urls import path, include
from rest_framework import routers

from .import views

router = routers.DefaultRouter()

router.register(r'staffs', views.StaffViewset)
router.register(r'users', views.UserViewset)
router.register(r'departments', views.DepartmentViewset)
router.register(r'vacancies', views.VacancymentViewset)
router.register(r'recruits', views.RecruitViewset)
router.register(r'recruitments', views.RecruitmentViewset)
router.register(r'attendance', views.AttendanceViewset)
router.register(r'documents', views.DocumentViewset)
router.register(r'announcements', views.AnnouncementViewset)
router.register(r'appointments', views.AppointmentViewset)
router.register(r'leaves', views.LeaveApplicationViewset)
router.register(r'payrol', views.PayrollViewset)

urlpatterns = [
    path('', include(router.urls)),
]

