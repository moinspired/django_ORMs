# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-19 12:09
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dojo_ninjas', '0002_auto_20171019_0806'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dojos',
            name='dojo_id',
        ),
    ]
