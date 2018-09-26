from django import forms

from ..models import Invigilator

class InvigilatorForm(forms.ModelForm):
    class Meta:
        model=Invigilator
        fields = ['name','dob','assignments']
        widgets = {'dob': forms.TextInput(attrs={'isDateField':True})}