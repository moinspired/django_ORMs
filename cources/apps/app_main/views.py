from __future__ import unicode_literals
from django.shortcuts import render,redirect
from .models import Course

def index(request):
    ctx = {'courses':Course.objects.all()}
    return render(request,'app_main/index.html',ctx)

def process(request):
    desc   = Description.objects.create(text=request.POST['description'])
    Course.objects.create(name=request.POST['name'],description=desc)

    return redirect('/')

def confirm_destroy(request,id):
    ctx = {'course':Course.objects.get(id=id)}
    return render(request,'app_main/confirm_destroy.html',ctx)

def destroy(request,id):
    Course.objects.get(id=id).delete()
    return redirect('/')
