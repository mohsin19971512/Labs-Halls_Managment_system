from pyexpat.errors import messages
from django.shortcuts import render,redirect,reverse
from . import forms,models
from django.db.models import Sum
from django.contrib.auth.models import Group
from django.http import HttpResponseRedirect
from django.core.mail import send_mail
from django.contrib.auth.decorators import login_required,user_passes_test
from datetime import datetime,timedelta,date
from django.conf import settings
from laboratories.models import Laboratorie
from halls.models import Day, Hall
from datetime import  time
from django.db.models import Q
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa
# Create your views here.


def convert_to_pdf(request,pk):
    halls=Hall.objects.get(id=pk)
    template_path = 'manage/pdf1.html'
    context = {'halls': halls}
    # Create a Django response object, and specify content_type as pdf
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="report.pdf"'
    # find the template and render it.
    template = get_template(template_path)
    html = template.render(context)

    # create a pdf
    pisa_status = pisa.CreatePDF(
       html, dest=response)
    # if error then show some funy view
    if pisa_status.err:
       return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response
    
    
def convert_to_pdf_lab(request,pk):
    halls=Laboratorie.objects.get(id=pk)
    template_path = 'manage/pdf1.html'
    context = {'halls': halls}
    # Create a Django response object, and specify content_type as pdf
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="report.pdf"'
    # find the template and render it.
    template = get_template(template_path)
    html = template.render(context)

    # create a pdf
    pisa_status = pisa.CreatePDF(
       html, dest=response)
    # if error then show some funy view
    if pisa_status.err:
       return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response

#for showing signup/login button for admin(by sumit)
def adminclick_view(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('afterlogin')
    return render(request,'manage/adminclick.html')



def admin_signup_view(request):
    form=forms.AdminSigupForm()
    if request.method=='POST':
        form=forms.AdminSigupForm(request.POST)
        if form.is_valid():
            user=form.save()
            user.set_password(user.password)
            user.save()
            my_admin_group = Group.objects.get_or_create(name='ADMIN')
            my_admin_group[0].user_set.add(user)
            return HttpResponseRedirect('adminlogin')
    return render(request,'manage/adminsignup.html',{'form':form})



def is_admin(user):
    return user.groups.filter(name='ADMIN').exists()


@login_required(login_url='adminlogin')
@user_passes_test(is_admin)
def home_view(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('afterlogin')
    return render(request,'manage/admin_dashboard.html')
def afterlogin_view(request):
    if is_admin(request.user):
        return redirect('admin-dashboard')
    
    

#---------------------------------------------------------------------------------
#------------------------ ADMIN RELATED VIEWS START ------------------------------
#---------------------------------------------------------------------------------
@login_required(login_url='adminlogin')
@user_passes_test(is_admin)
def admin_dashboard_view(request):
    
    laboratories=Laboratorie.objects.all().count()
    
    halls=Hall.objects.all().count()

    now = datetime.now()
    check_time =now.strftime("%I:%M")  #strftime("%I:%M %p")
    
    check_day =now.strftime("%A")



    hall_qs = []
    lab_qs = []
    free_qs = []
    new_qs = []
    if now.strftime("%p")=="PM":
        print("true")
        if check_time > time(10,30).strftime("%I:%M") and check_time < time(12,30).strftime("%I:%M")  :
            busy_time2 = Day.objects.filter(start_lect_tow__lte=check_time ,day = check_day)
            new_qs = busy_time2
            print("busy_time2",busy_time2)

        if  check_time > time(12,30).strftime("%I:%M") :
            busy_time3 = Day.objects.filter(end_lect_three__lte=time(2,00).strftime("%I:%M") ,day = check_day)
            #busy_time3 = Day.objects.filter(Q(start_lect_three>check_time and end_lect_three<check_time))
            
            new_qs = busy_time3
            print("busy_time3",busy_time3)
            
        if  check_time > time(1,00).strftime("%I:%M") and check_time < time(2,00).strftime("%I:%M") :
            busy_time3 = Day.objects.filter(start_lect_three__lte=check_time,day = check_day)
            new_qs = busy_time3
            print("busy_time3",busy_time3)

        if check_time > time(10,30).strftime("%I:%M") and check_time < time(12,30).strftime("%I:%M") :
            free_time2 = Day.objects.filter(start_lect_tow__isnull=True,day = check_day)
            free_qs = free_time2
            print("free_time2",free_time2)
            
        if  check_time > time(12,30).strftime("%I:%M") :
            free_time3 = Day.objects.filter(start_lect_three__isnull=True,day = check_day)
            free_qs = free_time3
            print("free_time3",free_time3)
            
        if  check_time > time(1,00).strftime("%I:%M") and check_time < time(2,00).strftime("%I:%M"):
            free_time3 = Day.objects.filter(start_lect_three__isnull=True,day = check_day)
            free_qs = free_time3
            print("free_time3",free_time3)

    else :
        print("AM")
        if check_time > time(8,30).strftime("%I:%M") and check_time < time(10,30).strftime("%I:%M"): 
            busy_time1 = Day.objects.filter(start_lect_one__isnull=False,start_lect_one__lte=check_time,end_lect_one__gte=check_time ,day = check_day)
            new_qs = busy_time1
            print("busy_time1",busy_time1)
        if check_time > time(10,30).strftime("%I:%M") and check_time < time(12,30).strftime("%I:%M")  :
            busy_time2 = Day.objects.filter(start_lect_tow__lte=check_time,day = check_day)
            new_qs = busy_time2
            print("busy_time2",busy_time2)


        if check_time > time(8,30).strftime("%I:%M") and check_time < time(10,30).strftime("%I:%M"): 
            free_time1 = Day.objects.filter(start_lect_one__isnull=True,day = check_day)
            free_qs = free_time1
            print("free_time1",free_time1)
        if check_time > time(10,30).strftime("%I:%M") and check_time < time(12,30).strftime("%I:%M") :
            free_time2 = Day.objects.filter(start_lect_tow__isnull=True,day = check_day)
            free_qs = free_time2
            print("free_time2",free_time2) 

    #new_qs = busy_time1|busy_time2|busy_time3
    #new_qs_2 = free_time1|free_time2|free_time3
    ava_hall_qs = []
    ava_lab_qs = []
    print(ava_lab_qs)
     
    for i in new_qs:
        
        h = Hall.objects.filter(days = i)
        if h.exists():
            hall_qs.append(h.first())
        else :
            print("Labro")
            
            l = Laboratorie.objects.filter(days = i)
            
            lab_qs.append(l.first())

    for j in free_qs:
        
        h = Hall.objects.filter(days = j)
        
        if h.exists():
            ava_hall_qs.append(h.first())

                
        else :
            print("Labro")
            l = Laboratorie.objects.filter(days = j)
            ava_lab_qs.append(l.first())
    print("check_time",check_time)
    print("check_day",check_day)
    
    print("ava_lab_qs",Day.objects.filter(start_lect_three__lte=check_time).first().start_lect_three)


    mydict={


    'hall_qs':hall_qs,
    'lab_qs':lab_qs,
    'ava_lab_qs':ava_lab_qs,
    'ava_hall_qs':ava_hall_qs,
    'available_hall' : len(ava_hall_qs),
    'available_lab' : len(ava_lab_qs),
    'laboratories':laboratories,
    'no_of_unavaliable_lab_now':len(lab_qs),
    'halls':halls,
    'no_of_avaliable_hall_now':len(hall_qs)
    }
    return render(request,'manage/admin_dashboard.html',context=mydict)



""" @login_required(login_url='adminlogin')
@user_passes_test(is_admin)
def hall_details(request,pk):
    halls=hall.objects.get(id=pk)
    context={
        "halls":halls,
    }
    return render(request,'manage/hall_details.html',context) """


@login_required(login_url='adminlogin')
@user_passes_test(is_admin)
def hall_details_2(request,pk):
    halls=Hall.objects.get(id=pk)
    context={
        "halls":halls,
    }
    return render(request,'manage/hall_detail.html',context) 

@login_required(login_url='adminlogin')
@user_passes_test(is_admin)
def edit_day(request,hall_id,pk):
    day=Day.objects.get(id=pk)
    if request.method == 'POST':
        form = forms.EditDay(request.POST, instance=day)
        if form.is_valid():
            form.save()
            return redirect('hall_detail', hall_id)      

    else:
        form = forms.EditDay(instance=day)

    return render(request,
                'manage/edit_day.html',
                {'form': form})


def delete_hall(request,pk):
    try:
        hall=Hall.objects.get(id=pk)
        if request.method == 'POST':
            hall.delete()
            return redirect('admin-view-hall')
    except:
        messages.error(request, "Hall Cannot be deleted  deleted ")
        return redirect('admin-view-hall')

    context={
        "hall":hall,
        "name":"Hall"

    }
    
    return render(request,'manage/sure_delete.html',context)

def delete_lab(request,pk):
    try:
        lab=Laboratorie.objects.get(id=pk)
        if request.method == 'POST':
            lab.delete()
            return redirect('admin-view-labs')
    except:
        messages.error(request, "Laboratorie Cannot be deleted  deleted ")
        return redirect('admin-view-labs')

    context={
        "lab":lab,
        "name":"Laboratorie"

    }
    
    return render(request,'manage/sure_delete_lab.html',context)

def delete_day(request,pk,hall_id):
    try:
        day=Day.objects.get(id=pk)
        if request.method == 'POST':
            day.delete()
            return redirect('hall_detail', hall_id)  
    except:
        messages.error(request, "Day Cannot be deleted  deleted ")
        return redirect('hall_detail', hall_id) 

    context={
        "day":day,
        "name":"Day"

    }
    
    return render(request,'manage/sure_delete_day.html',context)


def delete_day_lab(request,pk,lab_id):
    try:
        day=Day.objects.get(id=pk)
        if request.method == 'POST':
            day.delete()
            return redirect('lab_details', lab_id)  
    except:
        messages.error(request, "Day Cannot be deleted  deleted ")
        return redirect('lab_details', lab_id) 

    context={
        "day":day,
        "name":"Day"

    }
    
    return render(request,'manage/sure_delete_day.html',context)

@login_required(login_url='adminlogin')
@user_passes_test(is_admin)
def edit_day_in_lab(request,lab_id,pk):
    day=Day.objects.get(id=pk)
    if request.method == 'POST':
        form = forms.EditDay(request.POST, instance=day)
        if form.is_valid():
            form.save()
            return redirect('lab_details', lab_id)      

    else:
        form = forms.EditDay(instance=day)

    return render(request,
                'manage/edit_day.html',
                {'form': form})

@login_required(login_url='adminlogin')
@user_passes_test(is_admin)
def lab_details(request,pk):
    labs=Laboratorie.objects.get(id=pk)
    context={
        "labs":labs,
    }
    return render(request,'manage/lab_details.html',context)

# this view for sidebar click on admin page
@login_required(login_url='adminlogin')
@user_passes_test(is_admin)
def admin_hall_view(request):
    return render(request,'manage/admin_halls.html')



@login_required(login_url='adminlogin')
@user_passes_test(is_admin)
def admin_view_hall_view(request):
    hall_qs=Hall.objects.all()
    return render(request,'manage/admin_view_hall.html',{'hall_qs':hall_qs})





@login_required(login_url='adminlogin')
@user_passes_test(is_admin)
def admin_lab_view(request):
    return render(request,'manage/admin_lab.html')



@login_required(login_url='adminlogin')
@user_passes_test(is_admin)
def admin_view_lab_view(request):
    labs=Laboratorie.objects.all()
    return render(request,'manage/admin_view_labs.html',{'labs':labs})







