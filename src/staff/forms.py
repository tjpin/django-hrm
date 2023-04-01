from django import forms
from django.forms.widgets import NumberInput

from .models import Staff, GenderOptions, StaffPosition, EmployeeGrade, Department


class StaffRegistrationForm(forms.ModelForm):
    fields = "__all__"

    # doj = forms.CharField(widget=NumberInput(attrs={'class': 'input text-sm text-gray-500', 'type': 'date'}), label='')
    dob = forms.CharField(widget=NumberInput(attrs={'class': 'input text-sm text-gray-500', 'type': 'date'}), label='')
    bio = forms.CharField(
        widget=forms.Textarea(
            attrs={'class': 'border rounded px-2 py-2 resize-none text-gray-500 text-sm w-full', 'rows': 4}), 
        label='', required=False)
    files = forms.FileField(widget=forms.ClearableFileInput(attrs={'class': 'input', 'type': 'file', 'multiple':True}), required=False)
    # files = forms.CharField(widget=forms.ClearableFileInput(attrs={'class': 'input', 'type': 'file', 'multiple':True}), required=False)
    class Meta:
        model = Staff
        exclude = ['timetable', 'status', 'shift']

        widgets = {
            'doj': NumberInput(attrs={'class': 'input text-sm text-gray-500', 'type': 'date'}),
            'gender': forms.RadioSelect(choices=GenderOptions.choices)
        }
    
class DepartmentForm(forms.ModelForm):
    class Meta:
        model = Department
        fields = ['department']
    
class PositionForm(forms.ModelForm):
    class Meta:
        model = StaffPosition
        fields = ['position']
    
class GradeForm(forms.ModelForm):
    class Meta:
        model = EmployeeGrade
        fields = ['grade']


