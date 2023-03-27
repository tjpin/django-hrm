from django import forms
from django.forms.widgets import NumberInput

from .models import Application

class ApplicationForm(forms.ModelForm):
    # fields = ['first_name', 'middle_name', 'last_name', 'email', '']
    class Meta:
        model = ApplicationForm
        exclude = ['date_applied']