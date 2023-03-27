from rest_framework import (viewsets, permissions, authentication)

from .serializer import *
from src.account.models import AccountUser
from src.staff.models import Staff
from src.record.models import Document
from src.office.attendance import Attendance
from src.office.hrd import *


class StaffViewset(viewsets.ModelViewSet):
    queryset = Staff.objects.all().order_by('first_name')
    serializer_class = StaffSerializer
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [authentication.BasicAuthentication]


class UserViewset(viewsets.ModelViewSet):
    queryset =AccountUser.objects.all().order_by('first_name')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [authentication.BasicAuthentication]

class AttendanceViewset(viewsets.ModelViewSet):
    queryset = Attendance.objects.select_related('staff').order_by('date')
    serializer_class = AttendanceSerializer
    # permission_classes = [permissions.IsAuthenticated]
    # authentication_classes = [authentication.BasicAuthentication]

class DocumentViewset(viewsets.ModelViewSet):
    queryset = Document.objects.all()
    serializer_class = DocumentSerializer

# class RecruitmentViewset(viewsets.ModelViewSet):
#     queryset = None
#     serializer_class = None

# __________________ HRD ___________________________
class AppointmentViewset(viewsets.ModelViewSet):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer
    permission_classes = []

class AnnouncementViewset(viewsets.ModelViewSet):
    queryset = Announcement.objects.all()
    serializer_class = AnnouncementSerializer
    permission_classes = []

class LeaveApplicationViewset(viewsets.ModelViewSet):
    queryset = LeaveApplication.objects.all()
    serializer_class = LeaveApplicationSerializer
    permission_classes = []

# _____________ Recruitment ________________________
class RecruitViewset(viewsets.ModelViewSet):
    queryset = Recruit.objects.all()
    serializer_class = RecruitSerializer
    permission_classes = []

class RecruitmentViewset(viewsets.ModelViewSet):
    queryset = Recruitment.objects.all()
    serializer_class = RecruitmentSerializer
    permission_classes = []

class VacancymentViewset(viewsets.ModelViewSet):
    queryset = Vacancy.objects.all()
    serializer_class = VacancySerializer
    permission_classes = []
