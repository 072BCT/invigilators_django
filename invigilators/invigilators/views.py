from django.shortcuts import render, get_object_or_404,redirect
from django.http import HttpResponse,HttpResponseRedirect
from .models import *
from .forms import InvigilatorAssignmentChangeForm

# Create your views here.
def home(request):
    return HttpResponse("Hello World")





def invigilator_assignment_view(request):
    if request.method=='POST':
        form = InvigilatorAssignmentChangeForm(request.POST)
        if form.is_valid():
            invigilator_assignment = form.save(commit=False)
            invigilator_assignment.save()
            return redirect('invigilator_assignment_view')
    else:
        form = InvigilatorAssignmentChangeForm()
        return render(request,'assignmentChangeForm.html',{'form':form})



