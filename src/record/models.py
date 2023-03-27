import uuid, ntpath

from django.db import models
from django.utils import timezone
from django.conf import settings

from src.account.models import AccountUser
from src.staff.models import Staff
from utils.choice_helper import (DocumentStatus, DocumentTransmitalReason)
from utils.helper_functions import generate_id


class Document(models.Model):
    document = models.FileField(upload_to="records/uploads", null=True, blank=True)
    date_uploaded = models.DateField(default=timezone.now)
    reference_number = models.CharField(max_length=10, default=generate_id(10), unique=True)
    uploaded_by = models.ForeignKey(AccountUser, on_delete=models.CASCADE)

    @property
    def filename(self):
        return ntpath.basename(self.document.path)

    def __str__(self):
        return self.filename
    
    class Meta:
        ordering = ['date_uploaded', 'uploaded_by']


class Transmital(models.Model):
    transmital_number = models.CharField(max_length=20, unique=True, primary_key=True)
    document = models.ForeignKey(Document, on_delete=models.CASCADE)
    sent_to = models.ForeignKey(Staff, on_delete=models.CASCADE)
    sent_by = models.OneToOneField(AccountUser, on_delete=models.CASCADE)
    date_sent = models.DateField(default=timezone.now)
    date_returned = models.DateField(null=True, blank=True)
    is_returned = models.BooleanField(default=False, null=True, blank=True)
    status = models.CharField(max_length=15, choices=DocumentStatus.choices, default=DocumentStatus.TRANSMITED)
    reason_for_transmital = models.CharField(max_length=30, choices=DocumentTransmitalReason.choices, default=DocumentTransmitalReason.FOR_APPROVED)

    def __str__(self):
        return self.transmital_number
    
    class Meta:
        ordering = ['date_sent', 'transmital_number', 'status']
