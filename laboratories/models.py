from pyexpat import model
from secrets import choice
from tabnanny import verbose
from django.db import models
from halls.models import Day





class Laboratorie(models.Model):
    name = models.CharField(verbose_name="Name",max_length=250)
    supervisor = models.CharField(verbose_name="Supervisor",max_length=250,null=True,blank=True)
    numbers_of_computer = models.IntegerField(verbose_name="Numbers of Computer",null=True)
    working_computers = models.IntegerField(verbose_name="Working Computers",null=True)
    computers_not_working = models.IntegerField(verbose_name="Computers not working",null=True)
    data_show = models.BooleanField( verbose_name = "Data Show",default=True)
    days = models.ManyToManyField(Day)
    @property 
    def get_days(self):
        return self.days.all()

    def __str__(self) -> str:
        return f'{self.name }' 

"""     @property
    def lectures (self):
        return self.sunday.all().count()+self.monday.all().count()+self.tuesday.all().count()+self.Wednesday.all().count()+self.thursday.all().count()
 """
      

