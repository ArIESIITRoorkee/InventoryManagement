# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-02 03:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20170930_1841'),
    ]

    operations = [
        migrations.AlterField(
            model_name='equipmentinstance',
            name='buying_time',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
