# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-09-30 07:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='equipmentinstance',
            name='uid',
            field=models.CharField(blank=True, max_length=50, unique=True),
        ),
    ]