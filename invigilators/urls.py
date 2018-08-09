"""invigilators URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from invigilators.invigilators import views
from invigilators.invigilators import addViews, editViews , deleteViews
urlpatterns = [
    path('ajax/get_dates_and_shifts/',views.get_dates_and_shifts,name='get_dates_and_shifts'),
    path('admin/', admin.site.urls),
    path('',views.index, name='index'),
    path('exams/', views.exams_lv, name='exams_lv'),
    path('examinstances/', views.exam_instances_lv, name='exam_instances_lv'),
    path('invigilators/', views.invigilators_lv, name='invigilators_lv'),
    path('assignments/', views.assignments_lv, name='assignments_lv'),
    path('examrooms/', views.exam_rooms_lv, name='exam_rooms_lv'),
    path('dates/', views.exam_dates_lv, name='exam_dates_lv'),
    path('shifts/', views.exam_shifts_lv, name='shifts_lv'),
    path('exam_rooms_edit/<int:pk>',editViews.exam_rooms_edit,name='exam_rooms_edit'),
    path('exam_rooms_add/', addViews.exam_rooms_add, name='exam_rooms_add'),
    path('exam_rooms_remove/', deleteViews.exam_rooms_remove, name='exam_rooms_remove'),
    path('exams_edit/', editViews.exams_edit, name='exams_edit'),
    path('exams_add/', addViews.exams_add, name='exams_add'),
    path('exams_remove/', deleteViews.exams_remove, name='exams_remove'),
    path('exam_instances_edit/', editViews.exam_instances_edit, name='exam_instances_edit'),
    path('exam_instances_add/', addViews.exam_instances_add, name='exam_instances_add'),
    path('exam_instances_remove/', deleteViews.exam_instances_remove, name='exam_instances_remove'),
    path('assignments_edit/<int:pk>', editViews.assignments_edit, name='assignments_edit'),
    path('assignments_add/', addViews.assignments_add, name='assignments_add'),
    path('assignments_remove/', deleteViews.assignments_remove, name='assignments_remove'),


   # path('exam_dates_edit/', views.exam_dates_edit, name='exam_dates_edit'),
   # path('exam_dates_add/', views.exam_dates_add, name='exam_dates_add'),
    #path('exam_dates_remove/', views.exam_dates_remove, name='exam_dates_remove'),
]
