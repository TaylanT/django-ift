from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

# Create your models here.




# Create your models here.
class SignUp(models.Model):
	email = models.EmailField()
	full_name = models.CharField(max_length=120, blank=True, null=True)
	timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
	updated = models.DateTimeField(auto_now_add=False, auto_now=True)
	

	def __unicode__(self): #Python 3.3 is __str__
		return self.email
	



class ZeitErfassung(models.Model):
	beschreibung=models.CharField(max_length=120)
	start=models.DateTimeField()
	ende=models.DateTimeField()
	user = models.ForeignKey(User, null=True)
	dt=models.DurationField(null=True)
	timestamp = models.DateTimeField(auto_now_add=True, auto_now=False,null=True)

	

	def __str__(self): #Python 3.3 is __str__
		return self.beschreibung
	

	def timecalc(self):
		return ende - start

class Betreuer(models.Model):
	nachname=models.CharField(max_length=120)