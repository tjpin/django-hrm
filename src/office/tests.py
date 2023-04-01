from django.test import TestCase, RequestFactory, Client
from django.contrib.auth import authenticate, login
from django.contrib.auth.hashers import check_password, make_password
from django.utils import timezone

from .models import Appointment, AppointmentStatus
from .attendance import Attendance
from src.staff.models import StaffNextBirthday, Staff, EmployeeGrade, StaffPosition, Department
from .views import AttendanceView, AttendanceForm, DataExportForm
from src.account.models import AccountUser


class AppointmentTest(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.cl = Client()
        self.account = AccountUser.objects.create(
            email='admin@hrm.com'
        )
        self.account.set_password('admin.2023')
        self.account.save()
        self.appointment = Appointment.objects.create(
            appointment='Meeting',
            date=timezone.now(),
            details='AGM meetting',
            venue='Main Office'
        )
        self.position = StaffPosition.objects.create(position='Accountant')
        self.department = Department.objects.create(department='Technology')
        self.grade = EmployeeGrade.objects.create(grade='Grade 1')
        self.staff = Staff.objects.create(
            first_name='Jane',
            middle_name="SK",
            last_name="Doe",
            mobile_number=3265485,
            staff_number=23,
            email='jane@email.test',
            dob=timezone.now(),
            doj=timezone.now(),
            department=self.department,
            grade=self.grade,
            position=self.position
        )
        self.staff.save()
        self.attendance = Attendance.objects.create(
            date=timezone.now(),
            time_in=timezone.now().time(),
            break_time=timezone.now().time(),
            time_out=timezone.now().time(),
            staff=self.staff
        )
        self.department.save()
        self.position.save()
        self.grade.save()
        self.attendance.save()
        self.appointment.save()
    
    def test_appointment_created(self):
        self.assertTrue(Appointment.objects.exists(), True)
    
    def test_appointment_default_status(self):
        obj = Appointment.objects.first()
        self.assertEqual(obj.status, AppointmentStatus.PENDING)
    
    def test_appointment_date(self):
        obj = Appointment.objects.first()
        self.assertEqual(obj.date.date(), timezone.now().date())
    
    def test_attendance_staff(self):
        attendance = Attendance.objects.first()
        staff = Staff.objects.first()
        self.assertIsInstance(attendance.staff, (Staff,))

    # Views
    def test_attendance_home_request(self):
        request = self.factory.get('/attendance')
        view = AttendanceView.as_view()(request)
        self.assertEqual(view.status_code, 200)
    
    def test_attendance_context_name(self):
        view = AttendanceView()
        request = RequestFactory()
        view.setup(request)
        context = view.context_object_name
        self.assertEqual(context, 'attendances')

    def test_attendance_form(self):
        view = AttendanceView()
        request = RequestFactory()
        view.setup(request)
        form = view.form_class
        self.assertEqual(form, DataExportForm)


