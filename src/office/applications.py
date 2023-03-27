from datetime import datetime

from django.db import models
from django.utils import timezone

from utils.choice_helper import (LeaveStatus, LeaveChoices)
from src.staff.models import Staff


class LeaveApplication(models.Model):
    leave_type = models.CharField(max_length=10, choices=LeaveChoices.choices, default=LeaveChoices.ANNUAL)
    start_date = models.DateField()
    end_date = models.DateField()
    date_applied = models.DateField(default=timezone.now, null=True, blank=True)
    status = models.CharField(max_length=10, choices=LeaveStatus.choices, default=LeaveStatus.PENDING)
    staff = models.OneToOneField(Staff, on_delete=models.CASCADE)

    def __str__(self):
        return "{} {}".format(self.staff.first_name, self.staff.last_name)
    
    @property
    def days_applied(self):
        return datetime().now() + (self.end_date - self.start_date)

    class Meta:
        ordering = ['start_date', 'end_date', 'staff', 'status']
        verbose_name = 'Leave Application'
        verbose_name_plural = 'Leave Applications'