from django.db import models

# Create your models here.


class Exam(models.Model):
    title = models.CharField(max_length=255,unique=True)
    examRooms = models.ManyToManyField('ExamRoom',related_name='exams')

    def __str__(self):
        return self.title


class ExamDate(models.Model):
    class Meta:
        unique_together=(('date', 'exam'),)
    date = models.DateField(blank=False)
    exam = models.ForeignKey(Exam,on_delete=models.CASCADE,related_name="dates")

    def __str__(self):
        return str(self.date)


class Shift(models.Model):
    shiftName = models.CharField(max_length=255,blank=False,unique=True)
    exam = models.ForeignKey(Exam,on_delete=models.CASCADE,related_name="shifts")
    startTime = models.TimeField()
    endTime = models.TimeField()

    def __str__(self):
        return self.shiftName


class ExamRoom(models.Model):
    name = models.CharField(unique=True, max_length=255,blank=False)
    capacity = models.IntegerField(blank=False)

    def __str__(self):
        return self.name


class InvigilatorAssignment(models.Model):
    class Meta:
        unique_together = (('exam','date','shift'),)
    exam = models.ForeignKey(Exam,on_delete=models.CASCADE,related_name='invigilator_assignments')
    # related to invigilator with a reverse relation "invigilators"
    date = models.ForeignKey(ExamDate,on_delete=models.CASCADE,related_name='invigilator_assignments')
    shift = models.ForeignKey(Shift,on_delete=models.CASCADE,related_name='invigilator_assignments')

    def __str__(self):
        return self.exam.title


class Invigilator(models.Model):
    name = models.CharField(unique=True,max_length=255,blank=False)
    assignment = models.ForeignKey(InvigilatorAssignment,related_name='invigilators',blank=True,null=True,
                                   on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.name


class ExamInstance(models.Model):
    exam = models.ForeignKey(Exam, on_delete=models.DO_NOTHING, related_name='examInstances')
    date = models.ForeignKey(ExamDate, on_delete=models.DO_NOTHING, related_name='examInstances')
    shift = models.ForeignKey(Shift,on_delete=models.DO_NOTHING,related_name='examInstances')

    def __str__(self):
        return self.exam.title + " " + str(self.date) + " " + self.shift.shiftName
