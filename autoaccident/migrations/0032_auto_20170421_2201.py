# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-22 05:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('autoaccident', '0031_auto_20170421_1744'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='driver_license',
            field=models.CharField(max_length=8, null=True),
        ),
        migrations.AlterField(
            model_name='otherpartyinformation',
            name='otherparty_driver_license',
            field=models.CharField(max_length=8, null=True),
        ),
    ]
