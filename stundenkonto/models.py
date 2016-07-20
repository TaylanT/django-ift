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



    def berechnen(self, request):
        """Summiert stundenanzahl."""
        heute = datetime.date.today()
        aktueller_monat = heute.month
        zeit = ZeitErfassung.objects.filter(user__username=request.user,
                                 start__month=aktueller_monat).aggregate(test=Sum(F('dt')))
        # wenn vorhanden update
        if zeit['test']:
        
            zeit_stunden = zeit['test'].total_seconds()/3600
            obj, created = StatusUebersicht.objects.get_or_create(
                User_id=request.user.id,
                Monat=aktueller_monat,
                defaults={'User': request.user,
                          'Monat': aktueller_monat,
                          'Monatsstunden': zeit_stunden}
            )
            # t = StatusUebersicht.objects.get(User_id=request.user.id, Monat=aktueller_monat)
            
            # t.User = request.user
            # t.Monatsstunden = zeit_stunden  # change field
            # t.save()
        # wenn nicht vorhanden initialisieren
        if not zeit['test']:
            zeit_stunden = 0
            # t = StatusUebersicht.objects.get(User_id=request.user.id, Monat=aktueller_monat)
            obj, created = StatusUebersicht.objects.get_or_create(
                User=request.user,
                Monat=aktueller_monat,
                defaults={'User': request.user,
                          'Monat': aktueller_monat,
                          'Monatsstunden': zeit_stunden}
            )
            # t.User = request.user
            # # start datum
            # t.Monat = aktueller_monat
            # t.Monatsstunden = zeit_stunden  # change field
            # t.save()
        # TODO nonetype abfang hinzufuegen fuer erreichen status auch ohne eintrag
        return zeit_stunden

    def ueberhang(self, request):
        """Berechnung des Stundenueberhangs aus Vormonat."""
        aktueller_benutzer = MyUser.objects.get(username=request.user)
        Vertragsstunden_benutzer = aktueller_benutzer.Vertragstunden

        zeit_stunden = self.berechnen(request)

        t = StatusUebersicht.objects.get(User_id=request.user.id)
        t.Ueberhang = Vertragsstunden_benutzer-zeit_stunden 
        t.Monatsstunden = zeit_stunden
        t.User = request.user
        t.save()
        return t.Ueberhang
