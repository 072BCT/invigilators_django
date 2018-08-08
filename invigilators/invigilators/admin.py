from django.contrib import admin
from .models import *
import django.contrib.auth.admin
import django.contrib.auth.models
from django.contrib import auth
# Register your models here.


admin.site.unregister(auth.models.Group)
admin.site.unregister(auth.models.User)
admin.site.site_header = "Invigilators"
admin.site.index_title = "Invigilators\' database"
admin.site.site_title = "Invigilators"
admin.site.register(Exam)
admin.site.register(Invigilator)
admin.site.register(ExamRoom)
admin.site.register(ExamInstance)
admin.site.register(InvigilatorAssignment)
admin.site.register(ExamDate)
admin.site.register(Shift)

