# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-24 18:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_main', '0005_auto_20171024_1400'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trip',
            name='description',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='trip',
            name='destination',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='user',
            name='first_name',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='user',
            name='last_name',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='user',
            name='password',
            field=models.CharField(max_length=255),
        ),
    ]