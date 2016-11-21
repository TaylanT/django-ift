#!/usr/bin/python
          # -*- coding: latin-1 -*-
from __future__ import unicode_literals
import datetime
from django.db import models
from login.models import ZeitErfassung
from django.db.models import F, FloatField, Sum
from login.models import MyUser


class StatusUebersicht(models.Model):
    """Ueberblick uber aktuellen stundenstatus nach MTC."""
    Monatsstunden = models.FloatField(default=0)
    User = models.ForeignKey('login.MyUser', on_delete=models.CASCADE)
    Ueberhang = models.FloatField(default=0)
    Monat = models.IntegerField()
    
    def __str__(self): # Python 3.3 is __str__
        return '%s' %(self.User)


    def monat_anzeige(self):
        datum = datetime.datetime(2016, self.Monat, 1)
        return datum.strftime('%B')

    def get_aktuellermonat(self):
        heute = datetime.date.today()
        return heute.strftime("%B")



    def berechnen(self, request, monat):
        """Summiert stundenanzahl."""
        
        zeit = ZeitErfassung.objects.filter(user__username=request.user,
                                            start__month=monat).aggregate(test=Sum(F('dt')))
        
        # wenn vorhanden update
        if zeit['test']:

            zeit_stunden = zeit['test'].total_seconds() / 3600
            obj, created = StatusUebersicht.objects.get_or_create(
                User_id=request.user.id,
                Monat=monat,
                defaults={'Monatsstunden': zeit_stunden}
            )
        # wenn nicht vorhanden initialisieren
        if not zeit['test']:
            zeit_stunden = 0
            # t = StatusUebersicht.objects.get(User_id=request.user.id, Monat=aktueller_monat)
            obj, created = StatusUebersicht.objects.get_or_create(
                User=request.user,
                Monat=monat,
                defaults={'Monatsstunden': zeit_stunden}
            )
        return zeit_stunden


    
"""To Dos:
-Jahr mit hinzufügen
-buttons 
-view gestalten
-Datenbank design
""" 