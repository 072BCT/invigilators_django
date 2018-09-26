from django import forms
from ..models import ExamCenter
class ExamCenterForm(forms.ModelForm):
    class Meta:
        model=ExamCenter
        fields=['title']