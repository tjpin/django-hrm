from django.db import models

from src.staff.models import Staff

class StaffBirthday(models.Model):
    staff = models.ForeignKey(Staff, on_delete=models.CASCADE)

    def first_name(self):
        return self.staff.first_name

    def last_name(self):
        return self.staff.last_name

    def dob(self):
        return self.staff.dob
