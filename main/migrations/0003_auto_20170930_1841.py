# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-09-30 13:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20170930_1319'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='year',
            field=models.IntegerField(blank=True, default=0),
        ),
    ]
