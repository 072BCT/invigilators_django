from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.core.exceptions import ObjectDoesNotExist
from .models import *
from .formsDir.examRoomForm import ExamRoomForm
from .formsDir.assignmentsForm import AssignmentsForm
from django.contrib.auth import admin
from django.http import JsonResponse
from django.core import serializers

def exam_rooms_add(request):
    return None


def exams_add(request):
    return None


def exam_instances_add(request):
    return None


def assignments_add(request):
    return None