from django import forms

from .models import Document



class DocumentUploadForm(forms.ModelForm):
    document = forms.FileField(widget=forms.ClearableFileInput(attrs={'class': 'input', 'multiple': True}), label="Documents")
    # date_uploaded = forms.CharField(widget=forms.NumberInput(attrs={"class": 'input', 'type': 'date'}))

    class Meta:
        model = Document
        fields =["document"]

