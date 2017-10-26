# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'app_main/index.html')

def login(request):
    return render(request, 'app_main/sing_in.html')