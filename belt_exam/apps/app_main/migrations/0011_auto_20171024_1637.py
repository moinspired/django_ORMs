# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-24 20:37
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app_main', '0010_auto_20171024_1432'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trip',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='planned_trips', to='app_main.User'),
        ),
    ]
