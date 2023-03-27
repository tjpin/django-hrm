import ntpath

from django.db import models
from django.utils import timezone

from src.office.models import StaffPosition
from utils.choice_helper import RecruitStatus


class Vacancy(models.Model):
    vacancy = models.ForeignKey(
        StaffPosition, on_delete=models.SET_NULL, null=True, blank=True)
    description = models.TextField(max_length=1000, null=True, blank=True)
    number_of_vacancy = models.IntegerField(default=1)
    date_posted = models.DateField(default=timezone.now)
    application_deadline = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.vacancy.position

    class Meta:
        verbose_name = 'Vacancy'
        verbose_name_plural = 'Vacancies'


class BaseApplicant(models.Model):
    first_name = models.CharField(max_length=30)
    middle_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    mobile_number = models.IntegerField()
    email = models.CharField(max_length=50, blank=True, null=True)
    position = models.ForeignKey(
        Vacancy, on_delete=models.SET_NULL, null=True, blank=True)
    # date_applied = models.DateField(default=timezone.now)

    def __str__(self):
        pass

    @property
    def full_name(self):
        return "{} {}".format(self.first_name, self.last_name)

    class Meta:
        abstract = True


class Recruit(BaseApplicant):
    status = models.CharField(
        max_length=15, choices=RecruitStatus.choices, default=RecruitStatus.IN_REVIEW)
    # recruited_position = models.ForeignKey(Vacancy, related_name='recruited_vacancy', on_delete=models.SET_NULL, null=True, blank=True)
    date_recruited = models.DateField(default=timezone.now)

    def __str__(self):
        return "{} {}".format(self.first_name, self.last_name)

    class Meta:
        ordering = ['first_name', 'date_recruited']
        verbose_name = 'Recruit'
        verbose_name_plural = 'Recruits'


class Application(BaseApplicant):
    resume = models.FileField(upload_to='records/applications')
    message = models.TextField(max_length=500, null=True, blank=True)
    date_applied = models.DateField(default=timezone.now)

    def __str__(self):
        return self.full_name

    class Meta:
        ordering = ['date_applied']
        verbose_name = 'Application'
        verbose_name_plural = 'Applications'

    @property
    def resume_name(self):
        return ntpath.basename(self.resume.path)

    @property
    def position_applied(self):
        return self.applied_position.vacancy

    def clean(self):
        self.first_name.capitalize()
        self.middle_name.capitalize()
        self.last_name.capitalize()
        return super().clean(self)


class Recruitment(models.Model):
    vacancy = models.ForeignKey(
        Vacancy, 
        related_name='recruiting_vacancy',
                                on_delete=models.SET_NULL, null=True, blank=True)
    date = models.DateField()
    shortlisted = models.ManyToManyField(Recruit)

    def __str__(self):
        return self.vacancy.vacancy

    class Meta:
        verbose_name = 'Recruitment'
        verbose_name_plural = 'Recruitments'
