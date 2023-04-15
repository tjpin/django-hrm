from django.db import models
from django.conf import settings
from rest_framework import serializers

from src.account.models import AccountUser
from src.staff.models import Staff
from src.office.models import (
    EmployeeGrade, Department, StaffPosition, StaffShift)
from src.office.timesheet import Timetable
from src.office.attendance import Attendance
from src.office.hrd import Announcement, Payroll
from src.office.models import Appointment
from src.office.applications import LeaveApplication
from src.record.models import Document, Transmital
from src.recruitment.models import (Recruitment, Recruit, Application, Vacancy)
from .models import StaffBirthday


class GradeSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmployeeGrade
        fields = "__all__"


class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = "__all__"


class PositionSerializer(serializers.ModelSerializer):
    class Meta:
        model = StaffPosition
        fields = "__all__"


class ShiftSerializer(serializers.ModelSerializer):
    class Meta:
        model = StaffShift
        fields = "__all__"


class TimetableSerializer(serializers.ModelSerializer):
    class Meta:
        model = Timetable
        fields = "__all__"


# *****************************************************


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = AccountUser
        fields = ['first_name', 'last_name', 'email', 'mobile_number',
                  'date_joined', 'profile_picture', 'is_superuser', 'last_login', 'groups']


class StaffSerializer(serializers.ModelSerializer):
    position = PositionSerializer()
    department = DepartmentSerializer()
    shift = ShiftSerializer()
    grade = GradeSerializer()
    # timetable = TimetableSerializer()

    class Meta:
        model = Staff
        fields = "__all__"
        depth = 1


class BirthdaysSerializer(serializers.ModelSerializer):
    staff = StaffSerializer
    class Meta:
        model = StaffBirthday
        fields = ("first_name", 'last_name', 'dob')


class AttendanceSerializer(serializers.ModelSerializer):
    staff = StaffSerializer()

    class Meta:
        model = Attendance
        fields = "__all__"
        depth = 1


class DocumentSerializer(serializers.ModelSerializer):
    uploaded_by = UserSerializer()

    class Meta:
        model = Document
        fields = "__all__"
        depth = 1

# _____________ Recruitment ___________________


class VacancySerializer(serializers.ModelSerializer):
    vacancy = PositionSerializer()

    class Meta:
        model = Vacancy
        fields = "__all__"


class RecruitSerializer(serializers.ModelSerializer):
    position = PositionSerializer()

    class Meta:
        model = Recruit
        fields = "__all__"


class RecruitmentSerializer(serializers.ModelSerializer):
    vacancy = VacancySerializer()
    shortlisted = RecruitSerializer(many=True)

    class Meta:
        model = Recruitment
        fields = "__all__"

# _____________ HRD ___________________________


class AppointmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appointment
        fields = "__all__"


class AnnouncementSerializer(serializers.ModelSerializer):
    sender = UserSerializer()
    target = DepartmentSerializer(many=True)

    class Meta:
        model = Announcement
        fields = "__all__"


class LeaveApplicationSerializer(serializers.ModelSerializer):
    staff = StaffSerializer()

    class Meta:
        model = LeaveApplication
        fields = "__all__"


class PayrollSerializer(serializers.ModelSerializer):
    staff = StaffSerializer()

    class Meta:
        model = Payroll
        fields = "__all__"
