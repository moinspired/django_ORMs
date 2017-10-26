# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect

from .models import BirthDays

def index(request):
	birthdays = BirthDays.birthDayManager.all()
	return render(request, "date_app/index.html", {"birthdays": birthdays})

def process(request):
	BirthDays.birthDayManager.saveTheDate(request.POST)
	return redirect('/')
