# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect
from . models import User

# Create your views here.
def index(request):
    ctx = {
            'users':User.objects.all()
          }
    return render(request, 'app_main/index.html', ctx)

def add(request):
    print request.method
    print request.POST
    if request.method == 'GET':
        return render(request, 'app_main/new.html')
    elif request.method == 'POST':
        User.objects.create(first_name=request.POST['firstname'],last_name=request.POST['lastname'], email=request.POST['email'])
        return render(request, 'app_main/new.html')

def displayUser(request, id):
    conctex = {
        'user' : User.objects.get(id=id)
    }
    return render(request, 'app_main/show.html', conctex)


def editUser(request, id):
    if request.method == 'GET':
        conctex = {
            'user' : User.objects.get(id=id)
        }
        return render(request, 'app_main/edit.html', conctex)

    elif request.method == 'POST':
        currentUser = User.objects.get(id=id)
        currentUser.first_name=request.POST['firstname']
        currentUser.last_name=request.POST['lastname']
        currentUser.email=request.POST['email']
        currentUser.save()
        conctex = {
            'user' : User.objects.get(id=id)
        }
        return render(request, 'app_main/show.html', conctex)

def remove(request, id):
    User.objects.get(id=id).delete()
    return redirect('/')
