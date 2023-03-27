from datetime import timedelta, timezone
from django.db import models


class Timetable(models.Model):
    date = models.DateField()
    time_in = models.TimeField()
    time_out = models.TimeField()

    @property
    def staff(self):
        return self.staff_set.first()

    # @property
    # def status(self) -> str:
    #     state = None
    #     if self.staff:
    #         if timedelta(hours=self.staff.shift.time.hour) > timedelta(hours=self.time_in.hour) or self.time_out is not None:
    #             state = "out"
    #         # if timedelta(hours=self.staff.shift.time.hour) + timedelta(hours=1) < timedelta(hours=self.time_in.hour):
    #         if self.time_in is None and timedelta(hours=timezone.now().time.hour) + timedelta(hours=1) > timedelta(hours=self.staff.shift.time.hour):
    #             state = "absent"
    #         if (timedelta(hours=self.staff.shift.time.hour) + timedelta(hours=self.time_out.hour)) > timedelta(hours=self.staff.working_hours):
    #             state = "present"
    #         else:
    #             state = "in"
    #     return state

    @property
    def department(self):
        if self.staff:
            return self.staff.department
        return None

    @property
    def total_hours(self):
        t1 = timedelta(hours=self.time_out.hour, minutes=self.time_out.minute)
        t2 = timedelta(hours=self.time_in.hour, minutes=self.time_in.minute)
        return round(((t1 - t2).seconds) / 3600)

    def __str__(self):
        if self.staff:
            return "{} {}".format(self.staff.first_name, self.staff.last_name)
        return str(self.date)
    
    class Meta:
        verbose_name = 'Timetable'
        verbose_name_plural = 'Timetables'

