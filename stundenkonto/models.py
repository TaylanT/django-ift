#!/usr/bin/python
          # -*- coding: latin-1 -*-
from __future__ import unicode_literals
import datetime
from django.db import models
from login.models import ZeitErfassung
from django.db.models import F, FloatField, Sum
from login.models import MyUser

# Create your models here.
    

# class VertragsUebersicht(models.Model):

#     Vertragsstunden = models.CharField(max_length=120)
#     Vertragsstart = models.DateField(null=True)
#     Vertragsende = models.DateField(null=True)
#     # Ueberhang = models.FloatField(default=10.0)
# # class OffeneStunden(models.Model):


class StatusUebersicht(models.Model):
    """Ueberblick uber aktuellen stundenstatus nach MTC."""
    Monatsstunden = models.FloatField(default=0)
    User = models.ForeignKey('login.MyUser', on_delete=models.CASCADE,
    )
    Ueberhang = models.FloatField(default=0)
    Monat = models.IntegerField()
    
    def __str__(self): # Python 3.3 is __str__
        return '%s' %(self.User)

    def get_aktuellermonat(self):
        heute = datetime.date.today()
        return heute.strftime("%B")



    def berechnen(self, request, monat):
        """Summiert stundenanzahl."""
        heute = datetime.date.today()
        aktueller_monat = monat
        #print monat
        # aktueller_monat= 6
        zeit = ZeitErfassung.objects.filter(user__username=request.user,
                                 start__month=aktueller_monat).aggregate(test=Sum(F('dt')))
        # wenn vorhanden update
        if zeit['test']:
        
            zeit_stunden = zeit['test'].total_seconds()/3600
            obj, created = StatusUebersicht.objects.get_or_create(
                User_id=request.user.id,
                Monat=aktueller_monat,
                defaults={'Monatsstunden': zeit_stunden}
            )
        # wenn nicht vorhanden initialisieren
        if not zeit['test']:
            zeit_stunden = 0
            # t = StatusUebersicht.objects.get(User_id=request.user.id, Monat=aktueller_monat)
            obj, created = StatusUebersicht.objects.get_or_create(
                User=request.user,
                Monat=aktueller_monat,
                defaults={'Monatsstunden': zeit_stunden}
            )
        return zeit_stunden

    def ueberhang(self, request, monat):

        """Berechnung des Stundenueberhangs aus Vormonat."""
        # aktueller_monat= 6
        heute = datetime.date.today()
        aktueller_monat = monat
        aktueller_benutzer = MyUser.objects.get(username=request.user)
        Vertragsstunden_benutzer = aktueller_benutzer.Vertragstunden

        zeit_stunden = self.berechnen(request, monat)

        t = StatusUebersicht.objects.get(User_id=request.user.id, Monat=aktueller_monat)
        t.Ueberhang = Vertragsstunden_benutzer-zeit_stunden 
        t.Monatsstunden = zeit_stunden
        t.User = request.user
        t.save()
        return t.Ueberhang

"""To Dos:
-Jahr mit hinzufügen
-buttons 
-view gestalten
-Datenbank design
""" 