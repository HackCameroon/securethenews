# -*- coding: utf-8 -*-
# Generated by Django 1.9.9 on 2016-09-14 23:47
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sites', '0009_auto_20160914_2309'),
    ]

    operations = [
        migrations.AlterField(
            model_name='scan',
            name='site',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='scans', to='sites.Site'),
        ),
    ]
