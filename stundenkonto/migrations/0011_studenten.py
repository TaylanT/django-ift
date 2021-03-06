# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-19 11:41
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('stundenkonto', '0010_auto_20160720_1502'),
    ]

    operations = [
        migrations.CreateModel(
            name='Studenten',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vertragsstart', models.DateField(null=True)),
                ('vertragsende', models.DateField(null=True)),
                ('vertragstunden', models.IntegerField(null=True)),
                ('sollstunden', models.IntegerField(null=True)),
                ('iststunden', models.IntegerField(null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
