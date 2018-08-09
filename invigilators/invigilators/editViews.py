from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.core.exceptions import ObjectDoesNotExist
from .models import *
from .formsDir.examRoomForm import ExamRoomForm
from .formsDir.assignmentsForm import AssignmentsForm
from django.contrib.auth import admin
from django.http import JsonResponse
from django.core import serializers

def exam_rooms_edit(request,pk):
    examRoom = get_object_or_404(ExamRoom, pk=pk)
    form = ExamRoomForm(request.POST or None, instance=examRoom)
    if request.POST and form.is_valid():
        form.save()
        return redirect('exam_rooms_lv')

    return render(request, 'editviews/editViewsBase.html',
                  {'listViewUrl': reverse('exam_rooms_lv'), 'listViewName': 'Exam Rooms', 'name': 'Edit Exam Room',
                   'form': form})


def exams_edit(request):
    return None


def exam_instances_edit(request):
    return None


def assignments_edit(request,pk):
    assignment = get_object_or_404(InvigilatorAssignment,pk=pk)
    if not request.POST:
        form = AssignmentsForm(None,instance=assignment)
    elif request.POST:
        form = AssignmentsForm(request.POST)
        form.save()
        return redirect('assignments_lv')
    return render(request,'editviews/assignments_edit.html',
                  {'listViewUrl':reverse('assignments_lv'),
                   'listViewName':'Invigilator Assignments','name':'Edit Invigilator assignment','form':form})

