from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.core.exceptions import ObjectDoesNotExist
from .models import *
from .formsDir.examRoomForm import ExamRoomForm
from .formsDir.assignmentsForm import AssignmentsForm
from django.contrib.auth import admin
from django.http import JsonResponse
from django.core import serializers
# Create your views here.

def index(request):
    modelNamesAndUrls = [('Exam Dates', reverse('exam_dates_lv')), ('Shifts', reverse('shifts_lv')),
                         ('Exams', reverse('exams_lv')),
                         ('Exam Rooms', reverse('exam_rooms_lv')), ('Invigilators', reverse('invigilators_lv')),
                         ('Invigilator Assignments', reverse('assignments_lv'))]
    return render(request, 'index.html', {'modelNamesAndUrls': modelNamesAndUrls})


def get_all_objects(model):
    models = {}
    try:
        models = model.objects.all()
    except ObjectDoesNotExist:
        pass
    return models


def exams_lv(request):
    headings = ['Name']

    return render(request, 'listViews/exams_lv.html', {'name': 'Exams', 'objects': get_all_objects(Exam), 'headings': headings})


def invigilators_lv(request):
    headings = ['Name']
    return render(request, 'listViews/invigilators_lv.html', {'name': 'Invigilators',
                                                    'objects': get_all_objects(Invigilator), 'headings': headings})


def assignments_lv(request):
    headings = ['Exam', 'Date', 'Shift']
    return render(request, 'listViews/assignments_lv.html', {'name': 'Assign Invigilators',
                                                   'objects': get_all_objects(InvigilatorAssignment),
                                                   'headings': headings})


def exam_dates_lv(request):
    headings = ['Exam', 'Date']
    return render(request, 'listViews/exam_dates_lv.html', {'name': 'Exam Dates',
                                                  'objects': get_all_objects(ExamDate), 'headings': headings})


def exam_shifts_lv(request):
    headings = ['Name', 'Start Time', 'End Time']
    return render(request, 'listViews/exam_shifts_lv.html', {'name': 'Exam Shifts',
                                                   'objects': get_all_objects(Shift), 'headings': headings})


def exam_rooms_lv(request):
    headings = ['Name', 'Capacity']
    exam_rooms = get_all_objects(ExamRoom)
    return render(request, 'listViews/exam_rooms_lv.html', {'name': 'Exam Rooms', 'objects': exam_rooms, 'headings': headings})


def get_dates_and_shifts(request):
    examID = request.GET.get('pk',None)
    print(examID)
    exam = get_object_or_404(Exam,pk=examID)
    data = {
        'dates':serializers.serialize("json",exam.dates.all()),
        'shifts':serializers.serialize("json",exam.shifts.all())
    }
    return JsonResponse(data)
