# -*- coding: utf-8 -*-
# Generated by Django 1.11.dev20160912120730 on 2016-09-12 13:23
from __future__ import unicode_literals

import django.contrib.auth.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0003_auto_20160630_0839'),
    ]

    operations = [
        migrations.AddField(
            model_name='myuser',
            name='Initstunden',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='myuser',
            name='username',
            field=models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.ASCIIUsernameValidator()], verbose_name='username'),
        ),
    ]