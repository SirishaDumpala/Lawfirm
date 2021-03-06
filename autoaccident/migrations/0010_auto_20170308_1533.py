# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-08 23:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('autoaccident', '0009_auto_20170305_2226'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clientinstance',
            name='status',
            field=models.CharField(blank=True, choices=[('signinpending', 'Signin Pending'), ('propertydamage', 'Property Damage'), ('pendingmedicalreport', 'Pending Medical Report'), ('demand', 'Demand'), ('reject-1', 'Reject-1'), ('reject-2', 'Reject-2'), ('reject-3', 'Reject-3'), ('filed-in-court', 'Filed-in-Court'), ('closed', 'Closed'), ('other', 'Other')], default='pending', help_text='Case Status', max_length=50),
        ),
    ]
