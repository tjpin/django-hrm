from django import forms
from django.forms import NumberInput

from .system_settings import SystemSettings

class SettingsForm(forms.ModelForm):
    company_mobile_number = forms.CharField(widget=forms.NumberInput(
        attrs={'class': 'input', 'type': 'number', 'required': True}
    ))
    class Meta:
        fields = "__all__"
        model = SystemSettings



