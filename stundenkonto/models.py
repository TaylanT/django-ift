from __future__ import unicode_literals
import datetime
from django.db import models
from login.models import ZeitErfassung
from django.db.models import F, FloatField, Sum

# Create your models here.
    

# class VertragsUebersicht(models.Model):

#     Vertragsstunden = models.CharField(max_length=120)
#     Vertragsstart = models.DateField(null=True)
#     Vertragsende = models.DateField(null=True)
#     # Ueberhang = models.FloatField(default=10.0)
# # class OffeneStunden(models.Model):


class StatusUebersicht(models.Model):
    """Ueberblick uber aktuellen stundenstatus nach MTC."""
    Monatsstunden = models.FloatField()
    
    def berechnen(self, request):
        heute = datetime.date.today()
        aktueller_monat = heute.month
        zeit = ZeitErfassung.objects.filter(user__username=request.user,
                                 start__month=aktueller_monat).aggregate(test=Sum(F('dt')))
        zeit_stunden = zeit['test'].total_seconds()/3600
        self.Monatsstunden = zeit_stunden
        self.save()
        return zeit_stunden

