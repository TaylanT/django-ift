# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-06-14 14:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stundenkonto', '0002_vertragsuebersicht_ueberhang'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vertragsuebersicht',
            name='Ueberhang',
            field=models.FloatField(default=10.0),
        ),
    ]
