from django import forms
from ..models import ExamRoom


class ExamRoomForm(forms.ModelForm):
    class Meta:
        model = ExamRoom
        fields = ['name','capacity','examCenter']

