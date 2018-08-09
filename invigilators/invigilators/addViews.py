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

def exam_rooms_add(request):
    if request.method =='POST':
        form = ExamRoomForm(request.POST)
        if form.is_valid():
            examroom = form.save()
            return redirect('exam_rooms_lv')
    else:
        form = ExamRoomForm()
    return render(request, 'addViews/addViewBase.html', {'listViewUrl': reverse('exam_rooms_lv'),
                                                         'listViewName': 'Exam Rooms',
                                                         'name': 'Add New Exam Room',
                                                         'form': form})

def exams_add(request):
    if request.method =='POST':
        form = ExamForm(request.POST)
        if form.is_valid():
            exam = form.save()
            return redirect('exams_lv')
    else:
        form = ExamForm()
    return render(request,'addViews/addViewBase.html',{'listViewUrl':reverse('exams_lv'),
                                                        'listViewName':'Exams',
                                                       'name':'Add New Exam',
                                                       'form':form})



def assignments_add(request):
    if request.method =='POST':
        form = AssignmentsForm(request.POST)
        if form.is_valid():
            assignment = form.save()
            return redirect('assignments_lv')
    else:
        form = AssignmentsForm()
    return render(request, 'addViews/addViewBase.html', {'listViewUrl': reverse('assignments_lv'),
                                                         'listViewName': 'Assignments',
                                                         'name': 'Assign Invigilator',
                                                         'form': form})



def exam_dates_add(request):
    if request.method =='POST':
        form = ExamDateForm(request.POST)
        if form.is_valid():
            examdate = form.save()
            return redirect('exam_dates_lv')
    else:
        form = ExamDateForm()
    return render(request, 'addViews/addViewBase.html', {'listViewUrl': reverse('exam_dates_lv'),
                                                         'listViewName': 'Exam Dates',
                                                         'name': 'Add New Exam Date',
                                                         'form': form})




def shifts_add(request):
    if request.method =='POST':
        form = ShiftForm(request.POST)
        if form.is_valid():
            shift = form.save()
            return redirect('shifts_lv')
    else:
        form = ShiftForm()
    return render(request, 'addViews/addViewBase.html', {'listViewUrl': reverse('shifts_lv'),
                                                         'listViewName': 'Shifts',
                                                         'name': 'Add New Shift',
                                                         'form': form})


def invigilators_add(request):
    if request.method =='POST':
        form = InvigilatorForm(request.POST)
        if form.is_valid():
            invigilator = form.save()
            return redirect('invigilators_lv')
    else:
        form = InvigilatorForm()
    return render(request, 'addViews/addViewBase.html', {'listViewUrl': reverse('invigilators_lv'),
                                                         'listViewName': 'Invigilators',
                                                         'name': 'Add New Invigilator',
                                                         'form': form})