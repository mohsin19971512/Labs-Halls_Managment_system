from pyexpat import model
from random import choice
from tabnanny import verbose
from django.db import models

choice = (("Sunday","Sunday"),("Monday","Monday"),("Tuesday","Tuesday"),("Wednesday","Wednesday"),("Thursday","Thursday"))

class Hall(models.Model):
    name = models.CharField(verbose_name="Name",max_length=250)
    supervisor = models.CharField(verbose_name="supervisor",max_length=200,null=True,blank=True)
    seats = models.IntegerField(verbose_name="Seats",null=True)
    data_show = models.BooleanField( verbose_name = "Data Show",default=True)
    
    days = models.ManyToManyField('halls.Day')

    @property 
    def get_days(self):
        return self.days.all()

    class Meta:
        verbose_name = "Hall"
        verbose_name_plural = "Halls"

    def __str__(self) -> str:
        return f'{self.name}' 


class Day(models.Model):
    day = models.CharField(verbose_name="Day",choices=choice,max_length=50)
    lecture_one = models.CharField(verbose_name="lecture one",max_length=50,null=True,blank=True)
    lect_one_given_by = models.CharField(verbose_name="given by",max_length=50,null=True,blank=True)
    start_lect_one = models.TimeField(verbose_name="Start at",null=True,blank=True,auto_created=False)
    end_lect_one = models.TimeField(verbose_name="End at",null=True,blank=True,auto_created=False)
    lecture_tow = models.CharField(verbose_name="lecture tow",max_length=50,null=True,blank=True)
    lect_tow_given_by = models.CharField(verbose_name="given by",max_length=50,null=True,blank=True)
    start_lect_tow = models.TimeField(verbose_name="Start at",null=True,blank=True,auto_created=False)
    end_lect_tow = models.TimeField(verbose_name="End at",null=True,blank=True,auto_created=False)
    lecture_three = models.CharField(verbose_name="lecture three",max_length=50,null=True,blank=True,)
    lect_three_given_by = models.CharField(verbose_name="given by",max_length=50,null=True,blank=True)
    start_lect_three = models.TimeField(verbose_name="Start at",null=True,blank=True,auto_created=False)
    end_lect_three = models.TimeField(verbose_name="End at",null=True,blank=True,auto_created=False)


    def __str__(self) -> str:
        return f'{self.day}'



"""


choice = (("Sunday","Sunday"),("Monday","Monday"),("Tuesday","Tuesday"),("Wednesday","Wednesday"),("Thursday","Thursday"))
class Day(models.Model):
    day = models.CharField(verbose_name="Day",choices=choice,max_length=50)
    lectures = models.ManyToManyField(Lecture,related_name="a",null=True)

    
    def __str__(self) -> str:
        return f'{self.day }'




class hall(models.Model):
    name = models.CharField(verbose_name="Name",max_length=250)
    seats = models.IntegerField(verbose_name="Seats",null=True)

    #availability = models.CharField(max_length=100,choices=[("Available","Available"),("Unavailable","Unavailable")])
    days = models.ManyToManyField(Day)
    @property
    def Total_lectures(self):
        c = 0
        for i in self.days.all():
            c += i.lectures.count()

        return c

    @property 
    def get_days(self):
        return self.days.all()

    def __str__(self) -> str:
        return f'{self.name }'  



class Time(models.Model):
    start = models.TimeField(verbose_name="start at")
    end = models.TimeField(verbose_name="end at",auto_created=True)
    def __str__(self) -> str:
        return f'from {self.start } -  to {self.end }'

class Lecture(models.Model):
    branch = models.CharField(max_length=200,verbose_name="Branch")
    level = models.CharField(max_length=200,verbose_name="Level")
    subject_name = models.CharField(max_length=200,verbose_name="Subject Name")
    time = models.ForeignKey(Time,related_name='lectures',null=True,on_delete=models.SET_NULL)

    def __str__(self) -> str:
        return f'{self.subject_name }-{self.time}- {self.branch} - {self.level}'
"""