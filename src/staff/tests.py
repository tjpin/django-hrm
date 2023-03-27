from django.test import TestCase
from django.utils import timezone

from .models import StaffNextBirthday, Staff, EmployeeGrade, StaffPosition, Department

class StaffNextBirthdayTest(TestCase):
    def setUp(self):

        self.department = Department.objects.create(department='Finance')
        self.position = StaffPosition.objects.create(position='Accountant')
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

        self.department.save()
        self.position.save()
        self.grade.save()
        self.staff.save()

        self.birthday = StaffNextBirthday.upcoming_birthdays()

        self.staffs = Staff.objects.all()

    def test_birthdays_exists(self):
        self.assertTrue(self.birthday.count() == 1)
