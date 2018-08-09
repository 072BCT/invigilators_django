from django import forms

from ..models import Shift

class ShiftForm(forms.ModelForm):
    class Meta:
        model = Shift
        fields = ['shiftName','exam','startTime','endTime']