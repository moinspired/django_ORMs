# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-19 03:25
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0003_blog'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Blog',
        ),
        migrations.RemoveField(
            model_name='users',
            name='id_user',
        ),
    ]