from django.db import models

from utils.choice_helper import (AppointmentStatus)


class Department(models.Model):
    department = models.CharField(max_length=30)

    def __str__(self):
        return self.department


class EmployeeGrade(models.Model):
    grade = models.CharField(max_length=20)

    def __str__(self):
        return self.grade


class StaffPosition(models.Model):
    position = models.CharField(max_length=20)

    def __str__(self):
        return self.position


class StaffShift(models.Model):
    shift = models.CharField(max_length=20)
    time = models.TimeField(null=True, blank=True)
    date = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.shift

# #######################################################


class Appointment(models.Model):
    appointment = models.CharField(max_length=20)
    details = models.TextField(max_length=500, null=True, blank=True)
    date = models.DateTimeField()
    venue = models.CharField(max_length=20)
    status = models.CharField(
        max_length=20,
        choices=AppointmentStatus.choices,
        default=AppointmentStatus.PENDING)

    def __str__(self):
        return self.appointment

    class Meta:
        db_table = 'appointments'
        ordering = ['date', 'status']
        verbose_name = 'Appointment'
        verbose_name_plural = 'Appointments'
