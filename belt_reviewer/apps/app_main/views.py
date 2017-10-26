# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from django.contrib import messages
from .models import User


# Create your views here.

def index(request):
    return render(request, 'index.html')

def registerNewUser(request):
    errors = []
    if len(request.POST['firstname']) < 1:
        errors.append('Please enter name larger than 1 character')
    if len(request.POST['lastname']) < 1:
        errors.append('Please enter name larger than 1 character')
    if ValidateEmail(request.POST['email']) == False:
        errors.append('Please enter valid email')
    if len(request.POST['password']) < 6:
        errors.append('Please enter password larger than 6 character')
    if request.POST['password'] != request.POST['password_confermation']:
        errors.append('Password must match')
    if len(errors) < 1:
        user = User.userManager.create_user(
            firstname = request.POST['firstname'],
            lastname = request.POST['lastname'],
            email = request.POST['email'],
            password = request.POST['password'],
        )
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
        user = User.userManager.filter(email=request.POST['email'])
        request.session['first_name'] = user[0].first_name
        if len(user) > 0:
            if user[0].email == request.POST['email'] and user[0].password == request.POST['password']:
                return render(request, 'books.html')
            else:
                errors.append("Password doesn't match with the exiting email")
        else:
            errors.append("Password doesn't match with the exiting email")
    for error in errors:
            messages.add_message(request, messages.INFO, error)
    return redirect('/')


def add(request):
    return render(request, 'add.html')

def new_book(request):
    pass

def ValidateEmail( email ):    
    try:
        validate_email( email )
        return True
    except ValidationError:
        return False