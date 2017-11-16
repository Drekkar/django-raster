# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-11-16 10:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('raster', '0037_auto_20170509_0559'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rasterlayer',
            name='source_url',
            field=models.CharField(blank=True, default='', help_text='External url to get the raster file from. If a value is set,the rasterfile field will be ignored.', max_length=2500),
        ),
    ]
