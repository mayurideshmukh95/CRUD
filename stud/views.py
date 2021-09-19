from django.http.response import HttpResponse, HttpResponseRedirect
from stud.forms import StudentRegistration
from django.shortcuts import render
from .forms import StudentRegistration
from .models import User

def add_show(request):
    if request.method == 'POST':
        fm=StudentRegistration(request.POST)
        if fm.is_valid():
          nm = fm.cleaned_data['name']
          em = fm.cleaned_data['email']
          pw = fm.cleaned_data['password']
          reg =User(name=nm, email=em, password=pw)
          reg.save()
          fm=StudentRegistration()
    else:
        fm = StudentRegistration()
    stud = User.objects.all()
    return render(request, 'enroll/addandshow.html', {'form':fm, 'stu':stud})

def update_data(request,id):
    if request.method == 'POST':
       data = User.objects.get(pk=id) 
       fm = StudentRegistration(request.POST, instance=data)
       if fm.is_valid():
           fm.save()
    else:
        data = User.objects.get(pk=id) 
        fm = StudentRegistration(instance=data)
    return render(request,'enroll/updatestudent.html',{'form':fm})


def delete_data(request,id):
   if request.method == 'POST':
     data = User.objects.get(pk=id)
     data.delete()
     return HttpResponseRedirect('/')