from django import forms
from django.forms.widgets import NumberInput

from .models import Application, Recruit

class ApplicationForm(forms.ModelForm):
    # fields = ['first_name', 'middle_name', 'last_name', 'email', '']
    class Meta:
        model = Application
        exclude = ['date']

class RecruitForm(forms.ModelForm):
    date = forms.CharField(widget=forms.NumberInput(attrs={'class': 'input', 'type': 'date'}))

    class Meta:
        model = Recruit
        fields = "__all__"