# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from datetime import datetime

class BirthDayManager(models.Manager):
	def saveTheDate(self, post_data):
		if len(post_data["date"]) > 0:
			dob = datetime.strptime(post_data["date"], '%Y-%m-%d')
			if dob < datetime.now():
				BirthDays.birthDayManager.create(dob=dob)
				return True
		return False

class BirthDays(models.Model):
	dob = models.DateField()
	birthDayManager = BirthDayManager()
