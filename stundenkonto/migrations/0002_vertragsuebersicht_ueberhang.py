# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-06-14 14:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stundenkonto', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='vertragsuebersicht',
            name='Ueberhang',
            field=models.FloatField(default=0.0),
        ),
    ]