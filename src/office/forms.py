from django import forms

from .hrd import Training, Announcement, Payroll
from .models import Appointment, ExportChoices, ExportModel
from .attendance import Attendance


class TrainingForm(forms.ModelForm):
    class Meta:
        model = Training
        exclude = ['date', 'completed', 'data']

class AnnouncementForm(forms.ModelForm):
    message = forms.CharField(widget=forms.Textarea(attrs={'rows': 4, 'class': "border w-full rounded text-sm px-2 py-1"}))
    class Meta:
        model = Announcement
        exclude = ['date_announced', 'sender']



class AppointmentForm(forms.ModelForm):
    details = forms.CharField(widget=forms.Textarea(attrs={'rows': 4, 'class': "border w-full rounded text-sm px-2 py-1"}))
    date = forms.CharField(widget=forms.NumberInput(attrs={'class': 'input', 'type': 'datetime-local'}))
    class Meta:
        fields = "__all__"
        model = Appointment

class AttendanceForm(forms.ModelForm):
    date = forms.CharField(widget=forms.NumberInput(attrs={'class': 'input', 'type': 'date'}))
    time_in = forms.CharField(widget=forms.NumberInput(attrs={'class': 'input', 'type': 'time'}))
    break_time = forms.CharField(widget=forms.NumberInput(attrs={'class': 'input', 'type': 'time'}))
    time_out = forms.CharField(widget=forms.NumberInput(attrs={'class': 'input', 'type': 'time'}))
    # staff = forms.ModelChoiceField(
    #     queryset=Attendance.objects.all(),
    #     widget=forms.Select(attrs={'disabled': True})
    # )

    class Meta:
        fields = "__all__"
        model = Attendance

class DataExportForm(forms.ModelForm):
    export_format = forms.CharField(widget=forms.Select(choices=ExportChoices.choices))
    date = forms.CharField(widget=forms.NumberInput(attrs={"class": "input", "type": "date"}))
    class Meta:
        fields = "__all__"
        model = ExportModel


class PayrollForm(forms.ModelForm):
    pay_date = forms.CharField(widget=forms.NumberInput(attrs={"class": "input", "type": "date"}))

    class Meta:
        fields = "__all__"
        model = Payroll


