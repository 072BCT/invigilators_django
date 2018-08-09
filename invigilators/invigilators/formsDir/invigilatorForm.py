from django import forms

from ..models import Invigilator

class InvigilatorForm(forms.ModelForm):
    class Meta:
        model=Invigilator
        fields = ['name','assignment']