from django import forms
from django.forms import NumberInput

from .system_settings import SystemSettings

class SettingsForm(forms.ModelForm):
    class Meta:
        fields = "__all__"
        model = SystemSettings



