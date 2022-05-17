from logging import PlaceHolder
from django import forms
from django.contrib.auth.models import User

from halls.models import Day



#for admin signup
class AdminSigupForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['first_name','last_name','username','password']
        widgets = {
        'password': forms.PasswordInput()
        }


""" class TimeInput(forms.TimeField):
    input_type = "time" format='%I:%M %p'

    start_lect_one =forms.TimeField(widget=TimeInput(attrs={'placeholder': '8:30:pm'}),required=False)
    end_lect_one =forms.TimeField(widget=TimeInput(attrs={"class":"form-control"}),required=False) 
    start_lect_tow =forms.TimeField(widget=TimeInput(attrs={"class":"form-control"}),required=False)
    end_lect_tow =forms.TimeField(widget=TimeInput(attrs={"class":"form-control"}),required=False)
    start_lect_three =forms.TimeField(widget=TimeInput(attrs={"class":"form-control"}),required=False)
    end_lect_three =forms.TimeField(widget=TimeInput(attrs={"class":"form-control"}),required=False)    
    
    """

class TimeInput(forms.TimeInput):
    input_type = "time"
    
class EditDay(forms.ModelForm): 
    start_lect_one =forms.TimeField(widget=forms.TimeInput(attrs={'placeholder': '08:30 AM'}),required=False)
    end_lect_one =forms.TimeField(widget=forms.TimeInput(attrs={'placeholder': '10:30 AM'}),required=False)
    start_lect_tow =forms.TimeField(widget=forms.TimeInput(attrs={'placeholder': '10:30 AM'}),required=False)
    end_lect_tow =forms.TimeField(widget=forms.TimeInput(attrs={'placeholder': '12:30 AM'}),required=False)
    start_lect_three =forms.TimeField(widget=forms.TimeInput(attrs={'placeholder': '12:30 AM'}),required=False)
    end_lect_three =forms.TimeField(widget=forms.TimeInput(attrs={'placeholder': '02:00 AM'}),required=False)
    
    class Meta:
        model = Day
        fields = '__all__'
       






