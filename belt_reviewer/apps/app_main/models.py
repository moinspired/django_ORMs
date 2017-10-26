# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models

# Create your models here.

class UserManager(models.Manager):
    def create_user(self,firstname,lastname,email,password):
        return User.userManager.create(
                first_name = firstname,
                last_name = lastname,
                email = email,
                password = password
        )
    

    def login(self,email,password):
        return True

class AuthorManager(models.Manager):
    def add(self, first_name, last_name):
        return Author.userManager.create(
        first_name = first_name, 
        last_name = last_name                                
        )
class BookManager(models.Manager):
    def add(self, title):
        return  Author.userManager.create(title = title)
        
class User(models.Model):
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    email = models.CharField(max_length=45)
    password = models.CharField(max_length=45)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    userManager = UserManager()
class Author(models.Model):
    first_name = models.CharField(max_length=255)
    last_name  = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    manage = AuthorManager()
class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(Author)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    manage = BookManager
class Rating(models.Model):
    rating = models.IntegerField(default=170)
    book = models.ForeignKey(Book, related_name="books")
    user = models.ForeignKey(User, related_name="books")