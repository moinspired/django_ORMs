# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-24 18:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_main', '0006_auto_20171024_1408'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='trip',
            name='description',
        ),
        migrations.AddField(
            model_name='trip',
            name='note',
            field=models.TextField(default='default', max_length=255),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='user',
            name='password',
            field=models.CharField(max_length=45),
        ),
    ]
