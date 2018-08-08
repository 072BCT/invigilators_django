from django import forms
from ..models import *


class AssignmentsForm(forms.ModelForm):
    class Meta:
        model = InvigilatorAssignment
        fields = ['exam','date','shift']
