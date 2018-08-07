from django import forms
from .models import *


class InvigilatorAssignmentChangeForm(forms.ModelForm):
    class Meta:
        model = InvigilatorAssignment
        fields = ['exam','date','shift']
    def __init__(self,*args,**kwargs):
        super(InvigilatorAssignmentChangeForm,self).__init__(self,args,kwargs)

        try:
           dates = ExamDate.objects.filter(exam=self.instance.exam)
           shifts = Shift.objects.filter(exam=self.instance.exam)
           self.fields['date'].queryset = dates
           self.fields['shifts'].queryset = shifts
        except:
            pass
