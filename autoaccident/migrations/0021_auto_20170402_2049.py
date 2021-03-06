# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-03 03:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('autoaccident', '0020_remove_appointment_created_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='appointment',
            name='caller_first_name',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='appointment',
            name='caller_last_name',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='appointment',
            name='existing_client',
            field=models.BooleanField(default=False, help_text='Existing client?'),
        ),
    ]
