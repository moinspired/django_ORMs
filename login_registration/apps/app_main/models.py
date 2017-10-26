# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
import bcrypt

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
        
        user = User.userManager.filter(username=username)
        if len(user) ==  0:
            errors.append("Username not found!")
        if len(errors) > 0:
            return (False, errors)
        else:
            if bcrypt.checkpw(password.encode(), user[0].pw_hash.encode()):
                return (True, user)
            else:
                return (False, ["Incorrect Password!"])
           
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