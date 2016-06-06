# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-05 23:35
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('login', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Betreuer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vorname', models.CharField(max_length=120, null=True)),
                ('nachname', models.CharField(max_length=120, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='ZeitErfassung',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('beschreibung', models.CharField(max_length=120)),
                ('start', models.DateTimeField()),
                ('ende', models.DateTimeField()),
                ('dt', models.DurationField(null=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True, null=True)),
                ('betreuer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='login.Betreuer')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]