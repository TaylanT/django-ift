from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User


class Betreuer(models.Model):
	vorname=models.CharField(max_length=120,null=True)
	nachname=models.CharField(max_length=120,null=True)
	def __str__(self): #Python 3.3 is __str__
		return self.nachname


class ZeitErfassung(models.Model):
	beschreibung=models.CharField(max_length=120)
	start=models.DateTimeField()
	ende=models.DateTimeField()
	user = models.ForeignKey(User, null=True)
	betreuer = models.ForeignKey(Betreuer, null=True)
	dt=models.DurationField(null=True)
	timestamp = models.DateTimeField(auto_now_add=True, auto_now=False,null=True)

	

	def __str__(self): #Python 3.3 is __str__
		return self.beschreibung
	

	def timecalc(self):
		return ende - start


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    Vertragstunden = models.IntegerField()
    Vertragsstart = models.DateField()
    Vertragsende = models.DateField()


