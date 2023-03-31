from django.db import models
from django.conf import settings


class BaseSystemSettings(models.Model):
    company_name = models.CharField(max_length=30, null=True, blank=True)
    company_logo = models.ImageField(upload_to='settings/logo', null=True, blank=True)
    use_name = models.BooleanField(default=True)
    company_email = models.CharField(max_length=50, null=True, blank=True)
    company_address = models.CharField(max_length=50, null=True, blank=True)
    company_zip = models.CharField(max_length=50, null=True, blank=True)
    company_mobile_number = models.IntegerField(null=True, blank=True)
    currency = models.CharField(max_length=3, null=True, blank=True)

    def __str__(self):
        return self.company_name

    class Meta:
        abstract = True

class SystemSettings(BaseSystemSettings):    
    def __str__(self):
        return self.company_name
    
    class Meta:
        verbose_name = "System Settings"
        verbose_name_plural = "System Settings"
    

