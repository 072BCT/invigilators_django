from django.db import models

# Create your models here.
class Staff(models.Model):
    name = models.CharField(max_length=255,unique=True)

    def __str__(self):
        return self.name


class Exam(models.Model):
    title = models.CharField(max_length=255,unique=True)
    examDates = models.ManyToManyField('ExamDate',related_name="exams")

    def __str__(self):
        return self.title


class ExamDate(models.Model):

    date = models.DateField(blank=False,unique=True)

    def __str__(self):
        return str(self.date)


class Shift(models.Model):
    shiftName = models.CharField(max_length=255,blank=False,unique=True)

    def __str__(self):
        return self.shiftName


class ExamRoom(models.Model):
    name = models.CharField(unique=True, max_length=255,blank=False)
    capacity = models.IntegerField(blank=False)

    def __str__(self):
        return self.name


class InvigilatorAssignment(models.Model):
    class meta:
        unique_together = (('date','exam_room','shift'),)
    date = models.ForeignKey(ExamDate, blank=False, on_delete=models.DO_NOTHING, related_name='invigilatorAssignments')
    shift = models.ForeignKey(Shift,blank=False,on_delete=models.DO_NOTHING,related_name='+')
    exam_room = models.ForeignKey(ExamRoom,blank=False,on_delete=models.DO_NOTHING,related_name='invigilatorAssignments')

    def __str__(self):
        return str(self.date.date) + " "+self.shift.shiftName+" " +self.exam_room.name

class Invigilator(models.Model):
    staff = models.OneToOneField(Staff,related_name='invigilator',on_delete=models.DO_NOTHING)
    assignment = models.ForeignKey(InvigilatorAssignment,related_name='invigilators',blank=True,null=True, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.staff.name

class ExamInstance(models.Model):
    exam_room = models.ForeignKey(ExamRoom,on_delete=models.DO_NOTHING,related_name='examInstances')
    exam = models.ForeignKey(Exam, on_delete=models.DO_NOTHING, related_name='examInstances')
    date = models.ForeignKey(ExamDate, on_delete=models.DO_NOTHING, related_name='examInstances')
    shift = models.ForeignKey(Shift,on_delete=models.DO_NOTHING,related_name='examInstances')


    def __str__(self):
        return self.exam_room.name +" "+ self.exam.title +" "+ str(self.date.date)+" " +str(self.shift.shiftName)
