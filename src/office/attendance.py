from datetime import timedelta

from django.db import models

from src.staff.models import Staff


class Attendance(models.Model):
    date = models.DateField(null=True, blank=True)
    time_in = models.TimeField(null=True, blank=True)
    break_time = models.TimeField(null=True, blank=True)
    time_out = models.TimeField(null=True, blank=True)
    staff = models.ForeignKey(Staff, on_delete=models.CASCADE)

    @property
    def status(self) -> str:
        state = "-"
        if self.staff and self.staff.shift:
            if self.time_in is None and timedelta(hours=timezone.now().time.hour) + timedelta(hours=1) > timedelta(hours=self.staff.shift.time.hour):
                state = "absent"
            if (timedelta(hours=self.staff.shift.time.hour) + timedelta(hours=self.time_out.hour)) > timedelta(hours=self.staff.working_hours):
                state = "present"
            else:
                state = "-"
        return state

    @property
    def hours_worked(self):
        if self.time_in is not None and self.time_out is not None:
            return (timedelta(hours=self.time_out.hour-1) - timedelta(hours=self.time_in.hour))
            # return round(timedelta(hours=self.time_out.hour) - timedelta(hours=self.time_in.hour)) - 1 # minus 1hr for break time
        return 0

    def __str__(self):
        return "{} {}".format(self.staff.first_name, self.staff.last_name)

    class Meta:
        ordering = ['date', 'time_in', 'staff']
        verbose_name = 'Attendance'
        verbose_name_plural = 'Attendance'


