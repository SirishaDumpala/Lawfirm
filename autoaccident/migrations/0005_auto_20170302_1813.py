# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-03 02:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('autoaccident', '0004_clientaddress_client'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clientaddress',
            name='city',
            field=models.CharField(default='Fullerton', max_length=64, null=True, verbose_name='city'),
        ),
    ]