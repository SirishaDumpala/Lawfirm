# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-30 16:21
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('autoaccident', '0017_clientvehicle_carseat'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='otherpartyinformation',
            name='otherparty_Carseat',
        ),
    ]