from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.core.exceptions import ObjectDoesNotExist
from .models import *
from .formsDir.examRoomForm import ExamRoomForm
from .formsDir.assignmentsForm import AssignmentsForm
from .formsDir.examForm import ExamForm
from .formsDir.invigilatorForm import InvigilatorForm
from .formsDir.examDateForm import ExamDateForm
from .formsDir.shiftForm import ShiftForm
from django.contrib.auth import admin
from django.http import JsonResponse
from django.core import serializers
from django import template


register = template.Library()
@register.filter(name='field_type')
def get_field_type(field):
    return field.field.widget.__class__.__name__


def exam_rooms_edit(request,pk):
    examroom = get_object_or_404(ExamRoom, pk=pk)

    if request.method == 'POST':
        form = ExamRoomForm(request.POST, instance=examroom)
        if form.is_valid():
            examroom = form.save()
            return redirect('exam_rooms_lv')
    else:
        form = ExamRoomForm(instance=examroom)
    return render(request, 'editviews/editViewsBase.html', {'listViewUrl': reverse('exam_rooms_lv'),
                                                         'listViewName': 'Exam Rooms',
                                                         'name': 'Edit Exam Room',
                                                         'form': form})

def exams_edit(request,pk):
    exam = get_object_or_404(Exam, pk=pk)

    if request.method == 'POST':
        form = ExamForm(request.POST, instance=exam)
        if form.is_valid():
            exam = form.save()
            return redirect('exams_lv')
    else:
        form = ExamForm(instance=exam)
    return render(request, 'editviews/editViewsBase.html', {'listViewUrl':reverse('exams_lv'),
                                                        'listViewName':'Exams',
                                                       'name':'Edit Exam',
                                                       'form':form})



def assignments_edit(request,pk):
    assignment = get_object_or_404(InvigilatorAssignment,pk=pk)

    if request.method =='POST':
        form = AssignmentsForm(request.POST,instance=assignment)
        if form.is_valid():
            assignment = form.save()
            return redirect('assignments_lv')
    else:
        form = AssignmentsForm(instance=assignment)
    return render(request,'editviews/editViewsBase.html',{'listViewUrl': reverse('assignments_lv'),
                                                         'listViewName': 'Assignments',
                                                         'name': 'Change Invigilator Assignment',
                                                         'form': form})
def exam_dates_edit(request,pk):
    examdate = get_object_or_404(ExamDate, pk=pk)

    if request.method == 'POST':
        form = ExamDateForm(request.POST, instance=examdate)
        if form.is_valid():
            examdate = form.save()
            return redirect('exam_dates_lv')
    else:
        form = ExamDateForm(instance=examdate)
    return render(request, 'editviews/editViewsBase.html', {'listViewUrl': reverse('exam_dates_lv'),
                                                         'listViewName': 'Exam Dates',
                                                         'name': 'Edit Exam Date',
                                                         'form': form})


def shifts_edit(request,pk):
    shift = get_object_or_404(Shift, pk=pk)

    if request.method == 'POST':
        form = ShiftForm(request.POST, instance=shift)
        if form.is_valid():
            shift = form.save()
            return redirect('shifts_lv')
    else:
        form = ShiftForm(instance=shift)
    return render(request, 'editviews/editViewsBase.html', {'listViewUrl': reverse('shifts_lv'),
                                                         'listViewName': 'Shifts',
                                                         'name': 'Edit Shift',
                                                         'form': form})


def invigilators_edit(request,pk):
    invigilator = get_object_or_404(Invigilator, pk=pk)

    if request.method == 'POST':
        form = InvigilatorForm(request.POST, instance=invigilator)
        if form.is_valid():
            invigilator = form.save()
            return redirect('invigilators_lv')
    else:
        form = InvigilatorForm(instance=invigilator)
    return render(request, 'editviews/editViewsBase.html', {'listViewUrl': reverse('invigilators_lv'),
                                                         'listViewName': 'Invigilators',
                                                         'name': 'Add New Invigilator',
                                                         'form': form})


def examCenter_edit(request):
    return None