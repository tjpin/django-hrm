from django.db import models
from django.conf import settings
from django.contrib.auth import get_user, get_user_model

from src.staff.models import (HOD, Staff)
from src.account.models import AccountUser
from utils.helper_functions import parse_months
from utils.choice_helper import PayrollChoices
from .models import Department

class Performance(models.Model):
    staff = models.ForeignKey(Staff, on_delete=models.CASCADE, related_name='staff_performance')
    period = models.DateField()
    evaluator = models.ForeignKey(HOD, on_delete=models.CASCADE, related_name='performance_evaluator')
    score = models.CharField(max_length=10)
    comment = models.TextField(max_length=1000)

    @property
    def year(self):
        return self.period.year

    @property
    def month(self):
        return parse_months(self.period.month)
    
    def __str__(self):
        return "{}".format(self.staff)

class Payroll(models.Model):
    staff = models.ForeignKey(Staff, on_delete=models.CASCADE)
    basic_salary = models.DecimalField(default=0.00, decimal_places=2, max_digits=10)
    food_allowance = models.DecimalField(default=0.00, decimal_places=2, max_digits=10)
    house_allowance = models.DecimalField(default=0.00, decimal_places=2, max_digits=10)
    health_allowance = models.DecimalField(default=0.00, decimal_places=2, max_digits=10)
    transport_allowance = models.DecimalField(default=0.00, decimal_places=2, max_digits=10)
    other_allowance = models.DecimalField(default=0.00, decimal_places=2, max_digits=10)
    benefits = models.DecimalField(default=0.00, decimal_places=2, max_digits=10)
    overtime = models.DecimalField(default=0.00, decimal_places=2, max_digits=10)
    hourly_rate = models.DecimalField(default=0.00, decimal_places=2, max_digits=10)
    bonus = models.DecimalField(default=0.00, decimal_places=2, max_digits=10)
    deductions = models.DecimalField(default=0.00, decimal_places=2, max_digits=10)
    transaction_id = models.CharField(max_length=30, null=True, blank=True)
    month = models.CharField(max_length=30, null=True, blank=True)
    pay_date = models.DateField()
    status = models.CharField(max_length=10, choices=PayrollChoices.choices, default=PayrollChoices.PAID)

    def payment_date(self):
        return self.pay_date.strftime("%Y-%b-%d")

    def __str__(self):
        return "{} {}".format(self.staff.first_name, self.staff.last_name)
    
    @property
    def gross_salary(self):
        total_wages = (self.food_allowance + self.house_allowance + self.health_allowance + self.transport_allowance \
            + self.benefits + self.overtime + self.bonus + self.other_allowance + self.basic_salary) - self.deductions
        return total_wages

    class Meta:
        ordering = ['pay_date', 'staff']
        verbose_name = 'Payroll'
        verbose_name_plural = 'Payrolls'

class Training(models.Model):
    training = models.CharField(max_length=50)
    duration = models.CharField(max_length=20)
    date = models.DateField()
    venue = models.CharField(max_length=50)
    trainees = models.ManyToManyField(Staff)
    completed = models.BooleanField(default=False)
    data = models.JSONField()

    def __str__(self):
        return self.training
    
    class Meta:
        ordering = ['date', 'completed']
        verbose_name = 'Training'
        verbose_name_plural = 'Trainings'

class Announcement(models.Model):
    sender = models.ForeignKey(AccountUser, on_delete=models.CASCADE)
    target = models.ManyToManyField(Department())
    message = models.TextField(max_length=1000)
    subject = models.CharField(max_length=50)
    file = models.FileField(upload_to='records/anouncements', blank=True, null=True)
    date_announced = models.DateField(auto_now=True)

    def save(self, *args, **kwargs):
        self.sender = get_user_model().objects.first()
        return super(Announcement, self).save(*args, **kwargs)

    def __str__(self):
        return "{} - {} - {}".format(self.date_announced, self.sender, self.subject)
    
    class Meta:
        ordering = ['date_announced', 'sender']
        verbose_name = 'Announcement'
        verbose_name_plural = 'Announcements'

