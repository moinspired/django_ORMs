# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
# Create your models here.


class UserManager(models.Manager):
    def register(self,first_name,last_name,email,password,confirm):
        pass

    def login(self,email,password):
        pass

class User(models.Model):
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    email = models.CharField(max_length=45)
    password = models.CharField(max_length=45)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)