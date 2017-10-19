from __future__ import unicode_literals
from django.shortcuts import render,redirect
from .models import Course

def index(request):
    ctx = {'courses':Course.objects.all()}
    return render(request,'app_main/index.html',ctx)

def process(request):
    Course.objects.create(name=request.POST['name'],description=request.POST['desc'])
    return redirect('/')

def remove(request, id):
    Course.objects.get(id=id).delete()
    return redirect('/')
