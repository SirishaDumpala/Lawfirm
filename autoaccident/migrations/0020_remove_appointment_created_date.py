# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-02 13:28
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('autoaccident', '0019_appointment'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='appointment',
            name='created_date',
        ),
    ]
