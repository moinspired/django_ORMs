# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import User
# Create your views here.
def index(request):
    return render(request, 'app_main/index.html')

def register(request):
    errors = []
    firstname = request.POST['firstname']
    lastname = request.POST['lastname']
    email = request.POST['email']
    password = request.POST['password']
    password_confermation = request.POST['password_confermation']

    if len(firstname) < 1:
        errors.append('Name must be at least 2 characters long.')
    if len(lastname) < 1:
        errors.append('Name must be at least 2 characters long.')
    if len(email) < 1:
        errors.append('Email must be at least 2 characters long.')
    if len(request.POST['password']) < 5:
        errors.append('Password must be at least 5 characters long.')
    if request.POST['password'] != request.POST['password_confermation']:
        errors.append('Password must match.')

    if len(errors) < 1:
        user  = User.objects.create(
            first_name = firstname,
            last_name = lastname,
            email = email,
            password = password
        )
        request.session['id'] = user.id
        request.session['first_name'] = user.first_name
        redirect('/success')
    else:
        for error in errors:
            messages.add_message(request, messages.INFO, error)
    return redirect('/')

def login(request):
    errors = []     
    if len(request.POST['email']) < 1:
        errors.append('Email must be at least 2 characters long.')
    if len(request.POST['password']) < 5:
        errors.append('Password must be at least 5 characters long.')

    if len(errors) < 1:
        user = User.objects.filter(email=request.POST['email']).first()
        request.session['first_name'] = user.first_name

        if user:
            if user.email == request.POST['email'] and user.password == request.POST['password']:
                return redirect('/success')
            else:
                errors.append("Password doesn't match with the exiting email")
    for error in errors:
            messages.add_message(request, messages.INFO, error)
    return redirect('/')

def result(request):
    return render(request, 'app_main/success.html')

