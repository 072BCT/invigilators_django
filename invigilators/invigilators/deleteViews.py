from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.core.exceptions import ObjectDoesNotExist
from .models import *
from .formsDir.examRoomForm import ExamRoomForm
from .formsDir.assignmentsForm import AssignmentsForm
from django.contrib.auth import admin
from django.http import JsonResponse
from django.core import serializers

def exam_rooms_remove(request,pk):
    ExamRoom.objects.filter(pk=pk).delete()
    return JsonResponse({'message':'success'})

def exams_remove(request,pk):
    Exam.objects.filter(pk=pk).delete()
    return JsonResponse({'message': 'success'})

def assignments_remove(request,pk):
    InvigilatorAssignment.objects.filter(pk=pk).delete()
    print("removed assignment")
    return JsonResponse({'message': 'success'})

def exam_dates_remove(request,pk):
    ExamDate.objects.filter(pk=pk).delete()
    return JsonResponse({'message': 'success'})

def shifts_remove(request,pk):
    Shift.objects.filter(pk=pk).delete()
    return JsonResponse({'message': 'success'})


def invigilators_remove(request,pk):
    Invigilator.objects.filter(pk=pk).delete()
    return JsonResponse({'message': 'success'})