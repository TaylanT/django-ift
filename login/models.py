from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import AbstractUser


class Betreuer(models.Model):
    vorname = models.CharField(max_length=120, null=True)
    nachname = models.CharField(max_length=120, null=True)

    def __str__(self): # Python 3.3 is __str__
        return self.nachname


class MyUser(AbstractUser):

    # Username = models.CharField(max_length=40, unique=True)
    Vertragstunden = models.IntegerField(null=True)
    Vertragsstart = models.DateField(null=True)
    Vertragsende = models.DateField(null=True)

    # USERNAME_FIELD = 'Username'
    # REQUIRED_FIELDS = '__all__'


class ZeitErfassung(models.Model):

    beschreibung = models.CharField(max_length=120)
    start = models.DateTimeField()
    ende = models.DateTimeField()
    pause = models.DurationField()
    user = models.ForeignKey(MyUser, null=True)
    betreuer = models.ForeignKey(Betreuer, null=True)
    dt = models.DurationField(null=True)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False, null=True)
    Ueberhang = models.FloatField(default=10.0)

    def __unicode__(self):  # Python 3.3 is __str__
        """Convert into unicode so dass umlaute auch lesbar sind."""
        return u"%s" % self.beschreibung


    def timecalc(self):
        return ende - start
    def get_absolute_url(self):
            return u'/thanks/' 
 
