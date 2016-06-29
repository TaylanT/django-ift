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
    User = models.ForeignKey('login.MyUser', on_delete=models.CASCADE,
    )
    
    def __str__(self): # Python 3.3 is __str__
        return '%s' %(self.User)

    def berechnen(self, request):
        heute = datetime.date.today()
        aktueller_monat = heute.month
        zeit = ZeitErfassung.objects.filter(user__username=request.user,
                                 start__month=aktueller_monat).aggregate(test=Sum(F('dt')))
        udi=request.user
        udi.id
        t = StatusUebersicht.objects.get(User_id=request.user.id)
        
        zeit_stunden = zeit['test'].total_seconds()/3600
        #self.Monatsstunden = zeit_stunden
        t.User = request.user
        t.Monatsstunden = zeit_stunden  # change field
        t.save() # this will update only
        # TODO nonetype abfang hinzufuegen fuer erreichen status auch ohne eintrag

        
        return zeit_stunden

