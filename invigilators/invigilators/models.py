from django.db import models

# Create your models here.


class Exam(models.Model):
    title = models.CharField(max_length=255,unique=True)


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
        return self.exam.title+" "+self.shiftName


class ExamRoom(models.Model):
    name = models.CharField(unique=True, max_length=255,blank=False)
    capacity = models.IntegerField(blank=False)

    def __str__(self):
        return self.name


class InvigilatorAssignment(models.Model):
    class Meta:
        unique_together = (('exam','date','shift','examroom'),)
    exam = models.ForeignKey(Exam,on_delete=models.CASCADE,related_name='invigilator_assignments')
    # related to invigilator with a reverse relation "invigilators"
    date = models.ForeignKey(ExamDate,on_delete=models.CASCADE,related_name='invigilator_assignments')
    shift = models.ForeignKey(Shift,on_delete=models.CASCADE,related_name='invigilator_assignments')
    examroom = models.OneToOneField(ExamRoom,on_delete=models.CASCADE,null=True,unique=False)

    def __str__(self):
        return self.exam.title +" "+ str(self.date.date) + " "+ str(self.shift.shiftName)+" " +str(self.examroom.name)


class Invigilator(models.Model):
    name = models.CharField(unique=True,max_length=255,blank=False)
    assignments = models.ManyToManyField(InvigilatorAssignment,related_name='invigilators',blank=True,null=True,
                                   )
    examroom = models.ForeignKey(ExamRoom,related_name='invigilators',blank=True,null=True,on_delete=models.CASCADE)

    def __str__(self):
        return self.name


