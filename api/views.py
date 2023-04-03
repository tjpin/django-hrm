from rest_framework import (viewsets, permissions, authentication)
from rest_framework.generics import GenericAPIView, RetrieveUpdateDestroyAPIView
from rest_framework import renderers

from .serializer import *
from src.account.models import AccountUser
from src.staff.models import Staff
from src.record.models import Document
from src.office.attendance import Attendance
from src.office.hrd import *


class StaffViewset(RetrieveUpdateDestroyAPIView, viewsets.GenericViewSet):
    queryset = Staff.objects.all().order_by('first_name')
    serializer_class = StaffSerializer
    renderer_classes = [renderers.JSONRenderer]
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [authentication.BasicAuthentication, authentication.TokenAuthentication]

class UserViewset(viewsets.ModelViewSet):
    queryset =AccountUser.objects.all().order_by('first_name')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [authentication.BasicAuthentication, authentication.TokenAuthentication]

class AttendanceViewset(viewsets.ModelViewSet):
    queryset = Attendance.objects.select_related('staff').order_by('date')
    serializer_class = AttendanceSerializer
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [authentication.BasicAuthentication, authentication.TokenAuthentication]

class DocumentViewset(viewsets.ModelViewSet):
    queryset = Document.objects.all()
    serializer_class = DocumentSerializer
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [authentication.BasicAuthentication, authentication.TokenAuthentication]

class DepartmentViewset(viewsets.ModelViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [authentication.BasicAuthentication, authentication.TokenAuthentication]

# __________________ HRD ___________________________
class AppointmentViewset(viewsets.ModelViewSet):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [authentication.BasicAuthentication, authentication.TokenAuthentication]

class AnnouncementViewset(viewsets.ModelViewSet):
    queryset = Announcement.objects.all()
    serializer_class = AnnouncementSerializer
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [authentication.BasicAuthentication, authentication.TokenAuthentication]

class LeaveApplicationViewset(viewsets.ModelViewSet):
    queryset = LeaveApplication.objects.all()
    serializer_class = LeaveApplicationSerializer
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [authentication.BasicAuthentication, authentication.TokenAuthentication]

class PayrollViewset(viewsets.ModelViewSet):
    queryset = Payroll.objects.all()
    serializer_class = PayrollSerializer
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [authentication.BasicAuthentication, authentication.TokenAuthentication]

# _____________ Recruitment ________________________
class RecruitViewset(viewsets.ModelViewSet):
    queryset = Recruit.objects.all()
    serializer_class = RecruitSerializer
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [authentication.BasicAuthentication, authentication.TokenAuthentication]

class RecruitmentViewset(viewsets.ModelViewSet):
    queryset = Recruitment.objects.all()
    serializer_class = RecruitmentSerializer
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [authentication.BasicAuthentication, authentication.TokenAuthentication]

class VacancymentViewset(viewsets.ModelViewSet):
    queryset = Vacancy.objects.all()
    serializer_class = VacancySerializer
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [authentication.BasicAuthentication, authentication.TokenAuthentication]
