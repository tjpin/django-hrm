from dateutil.relativedelta import relativedelta
from datetime import timedelta

from django.db import models
from django.db.models import Q
from django.utils import timezone

from utils.choice_helper import (EducationChoices, StaffStatusChoices, LeaveStatus, LeaveChoices, GenderOptions)
from src.office.models import (Department, EmployeeGrade, StaffPosition, StaffShift)
from src.office.timesheet import Timetable
# from src.office.hrd import Payroll
# from src.office.attendance import Attendance


class Staff(models.Model):
    first_name = models.CharField(max_length=20)
    middle_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    mobile_number = models.IntegerField()
    email = models.EmailField(max_length=50, null=True, blank=True, unique=True)
    picture = models.ImageField(null=True, blank=True, upload_to='staffs/profiles')
    staff_number = models.CharField(max_length=10, unique=True)
    bio = models.CharField(max_length=500, null=True, blank=True)
    gender = models.CharField(max_length=10, choices=GenderOptions.choices, default=GenderOptions.OTHER)
    dob = models.DateField()
    doj = models.DateField()
    working_hours = models.PositiveIntegerField(null=True, blank=True, default=10)
    education = models.CharField(max_length=20, choices=EducationChoices.choices, default=EducationChoices.DIPLOMA)
    status = models.CharField(max_length=20, choices=StaffStatusChoices.choices, default=StaffStatusChoices.ACTIVE)

    grade = models.ForeignKey(EmployeeGrade, on_delete=models.CASCADE)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    position = models.ForeignKey(StaffPosition, on_delete=models.CASCADE)
    shift = models.ForeignKey(StaffShift, on_delete=models.SET_NULL, null=True, blank=True)
    timetable = models.ManyToManyField(Timetable, blank=True)
    
    class Meta:
        ordering = ['first_name', 'doj', 'staff_number']
        verbose_name = 'Staff'
        verbose_name_plural = 'Staffs'

    def __str__(self):
        return "{} {} {}".format(self.first_name, self.middle_name, self.last_name)
    
    def clean(self):
        self.first_name = self.first_name.capitalize()
        self.middle_name = self.middle_name.capitalize()
        self.last_name = self.last_name.capitalize()
    
    @property
    def full_name(self):
        return self.__str__()
    
    def hod(self):
        hod = HOD.objects.get(hod__department=self.department)
        if hod:
            return hod.hod
        else:
            return "-"
    
    def attendance_record(self):
        return self.attendance_set.all()
    
    def staff_files(self):
        return self.staff_file.all()

    @property
    def payroll(self):
        return self.payroll_set.select_related('staff').filter(staff__id=self.id)
    

class HOD(models.Model):
    hod = models.ForeignKey(Staff, on_delete=models.CASCADE, related_name='department_head')

    def __str__(self):
        return "{} {}".format(self.hod.first_name, self.hod.last_name)

    def department(self):
        return self.hod.department.department
    
    def hod_name(self):
        return self.hod.full_name()


class StaffNextBirthday(Staff):
    class Meta:
        proxy = True
    
    @classmethod
    def upcoming_birthdays(cls):
        today = timezone.now()
        three_days = today + timedelta(days=3)
        return cls.objects.filter(dob__range=(today, three_days)).order_by('dob')

    """"
        Below filters works with sqlite3 database. Above works well with postgresql.

        def upcoming_birthdays(self):
            curent_year = timezone.now().year
            curent_month = timezone.now().month

            curent_day = timezone.now().day
            third_day =(timezone.now() + timedelta(days=3)).day
            return self.objects.filter(
                Q(dob__year__iexact=curent_year) & 
                Q(dob__month__iexact=curent_month) & 
                Q(dob__day__iexact=curent_day) | Q(dob__day__iexact=third_day-1) |
                Q(dob__day__iexact=third_day)
            ).order_by('dob')
    """
    


