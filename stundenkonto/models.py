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
    Monatsstunden = models.FloatField()
    User = models.ForeignKey('login.MyUser', on_delete=models.CASCADE,
    )
    Ueberhang = models.FloatField(default=0)
    
    def __str__(self): # Python 3.3 is __str__
        return '%s' %(self.User)

    def berechnen(self, request):
        heute = datetime.date.today()
        aktueller_monat = heute.month
        zeit = ZeitErfassung.objects.filter(user__username=request.user,
                                 start__month=aktueller_monat).aggregate(test=Sum(F('dt')))
        
        t = StatusUebersicht.objects.get(User_id=request.user.id)
        
        zeit_stunden = zeit['test'].total_seconds()/3600
        #self.Monatsstunden = zeit_stunden
        t.User = request.user
        t.Monatsstunden = zeit_stunden  # change field
        t.save() # this will update only
        # TODO nonetype abfang hinzufuegen fuer erreichen status auch ohne eintrag
        return zeit_stunden
    def ueberhang(self, request):
        """Berechnung des Stundenueberhangs aus Vormonat."""
        aktueller_benutzer = MyUser.objects.get(username=request.user)
        Vertragsstunden_benutzer = aktueller_benutzer.Vertragstunden

        zeit_stunden = self.berechnen(request)

        t = StatusUebersicht.objects.get(User_id=request.user.id)
        t.Ueberhang = zeit_stunden -Vertragsstunden_benutzer-self.Ueberhang
        t.Monatsstunden=zeit_stunden
        t.User = request.user
        #self.save(update_fields=["Ueberhang"])
        t.save()
        return t.Ueberhang



        
        

