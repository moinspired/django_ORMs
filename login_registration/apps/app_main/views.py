# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect
from .models import User
from django.contrib import messages

def index(request):
    return render(request, 'index.html')

def new_user(request):
    valid = User.userManager.register(
        request.POST['username'],
        request.POST['password'],
        request.POST['confirm']
    )
    if valid[0]:
        pass
    else:
        for error in valid[1]:
            messages.add_message(request, messages.INFO, error)
    print valid
    return redirect('/')
def new_session(request):
    valid = User.userManager.login(
        request.POST['username'],
        request.POST['password']
    )
    if valid[0]:
            pass
    else:
        for error in valid[1]:
            messages.add_message(request, messages.INFO, error)
    return redirect('/')