from django import forms
from ..models import ExamDate
class ExamDateForm(forms.ModelForm):
    class Meta:
        model=ExamDate
        fields=['date','exam']
