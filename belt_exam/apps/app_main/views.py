# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect
from .models import User, Trip, Join
from django.contrib import messages

def index(request):
    return render(request, 'index.html')

def register(request):
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
def login(request):
    valid = User.userManager.login(
        request.POST['username'],
        request.POST['password']
    )
    if valid[0]:
        request.session['username'] = valid[1][0].username
        request.session['id'] = valid[1][0].id
        return redirect('/dashboard')
    else:
        for error in valid[1]:
            messages.add_message(request, messages.INFO, error)
    return redirect('/')

def dashboard(request):
        all_trips = Trip.objects.all()
        joins = Join.objects.filter(user_id = request.session['id'])

        for join in joins:
           all_trips = all_trips.exclude(id=join.trip.id)

        
        ctx =  {
           "trips": Trip.objects.filter(user_id=request.session['id']), #logged in person's trip
           "all_Trips": Trip.objects.all(),
           "joins" : joins,
           "excluded_trips": all_trips
        }

        print ctx['excluded_trips']
        return render(request, 'dashboard.html', ctx)

def add(request):
    return render(request, 'add.html')

def create(request):
    valid = Trip.objects.validateTrip(request.POST, request.session['id'])

    if valid[0]:
        return redirect('/add')
    else:
        for error in valid[1]:
            messages.add_message(request, messages.INFO, error)
        return redirect('/add')

def destination(request, id):
    #getting all the joined trip with the existing user id
    all_trip = Trip.objects.exclude(id=id)
    all_join = Join.objects.filter(trip_id=id)

    names = []
    for join in all_join:
        if join.user.username != request.session['username']:
            names.append(join.user.username)

    trip = Trip.objects.get(id=id)
    user = User.userManager.get(id=trip.user_id)
    
    ctx =  {
        "trip": trip,
        "user": user,
        'exclude_trip': Join.objects.filter(trip_id=all_join[0].trip),
        'names': names
    }

    return render(request, 'destination.html', ctx)


def join(request, id):
    Join.objects.create(
        user_id = request.session['id'],
        trip_id = id
    )
    return redirect("/dashboard")

def logout(request):
    request.session.delete()
    return redirect('/')