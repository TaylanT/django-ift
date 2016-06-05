from __future__ import unicode_literals

from django.db import models

# Create your models here.

class VertragsUebersicht(models.Model):
	Vertragsstunden=models.CharField(max_length=120)
	Vertragsstart=models.DateField()
	Vertragsende=models.DateField()
	
	
