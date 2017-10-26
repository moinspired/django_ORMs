# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
import bcrypt
from datetime import datetime

now = str(datetime.now())

class UserManager(models.Manager):
    def register(self, username, password, confirm):
        print "inside my models.py", username, password, confirm
        errors = []

        if len(username) < 2:
            errors.append("Username must be 2 characters or longer")
        elif len(User.userManager.filter(username=username)) > 0:
            errors.append("Username already exists!")
        if len(password) < 5:
            errors.append("password must be 5 characters or longer")
        if not password == confirm:
            errors.append("password must match Confirm Password")
        
        if len(errors) > 0:
            return (False, errors)
        else:
            pw_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
            user = User.userManager.create(username = username, pw_hash=pw_hash)
            return (True, user)

    def login(self, username, password):
        errors = []

        if len(username) < 2:
            errors.append("Username must be 2 characters or longer")
        if len(password) < 5:
            errors.append("password must be 5 characters or longer")
        
        user = User.userManager.filter(username=username) #returns list of user objects
        print "*********************User: {}".format(user)
        if len(user) ==  0:
            errors.append("Username not found!")
        if len(errors) > 0:
            return (False, errors)
        else:
            if bcrypt.checkpw(password.encode(), user[0].pw_hash.encode()):
                return (True, user)
            else:
                return (False, ["Incorrect Password!"])

class TripManager(models.Manager):
    def validateTrip(self, form, user_id):
        destination = form['destination']
        description = form['description']
        start_date = form['start_date']
        end_date = form['end_date']

        errors = []

        if len(destination) < 2:
            errors.append("The destination must be 2 characters or more.")
        if len(description) < 2:
            errors.append("The description must be 2 characters or more.")
        if not start_date:
            errors.append("Please enter start date")
        elif start_date < now:
            errors.append("Time cannot be in the past")
        if not end_date:
            errors.append("Please enter end date")
        elif end_date < start_date:
            errors.append("End date cannot be before start date")


        if len(errors) > 0:
            print errors
            return (False, errors)
        else:
            trip = Trip.objects.create(
                destination = destination, 
                description = description,
                start_date = start_date,
                end_date = end_date,
                user_id = user_id
                )
            Join.objects.create(user_id=user_id, trip_id=trip.id)
            return (True, trip)
       
        
class User(models.Model): 
    username = models.CharField(max_length=255)
    pw_hash = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    userManager = UserManager()

    def __repr__(self):
        return "<user object: {} {} {}".format(
            self.username,
            self.created_at,
            self.updated_at
    )

class Trip(models.Model):
    destination = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, related_name="trips")

    objects = TripManager()

class Join(models.Model):
    user = models.ForeignKey(User, related_name="users")
    trip = models.ForeignKey(Trip, related_name="trip")