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
    return render(request,'addViews/exam_rooms_add.html',{})

def exams_add(request):
    if request.method =='POST':
        form = ExamForm(request.POST)
        if form.is_valid():
            exam = form.save()
            return redirect('exams_lv')
    else:
        form = ExamForm()
    return render(request,'addViews/exam_add.html',{})


def assignments_add(request):
    if request.method =='POST':
        form = AssignmentsForm(request.POST)
        if form.is_valid():
            assignment = form.save()
            return redirect('assignments_lv')
    else:
        form = AssignmentsForm()
    return render(request,'addViews/assignments_add.html',{})



def exam_dates_add(request):
    if request.method =='POST':
        form = ExamDateForm(request.POST)
        if form.is_valid():
            examdate = form.save()
            return redirect('exam_dates_lv')
    else:
        form = ExamDateForm()
    return render(request,'addViews/examdates_add.html',{})




def shifts_add(request):
    if request.method =='POST':
        form = ShiftForm(request.POST)
        if form.is_valid():
            shift = form.save()
            return redirect('shifts_lv')
    else:
        form = AssignmentsForm()
    return render(request,'addViews/shifts_add.html',{})


def invigilators_add(request):
    return None