# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-14 21:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('autoaccident', '0027_claiminfo_otherpartyclaim'),
    ]

    operations = [
        migrations.AddField(
            model_name='calllog',
            name='date_of_accident',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
