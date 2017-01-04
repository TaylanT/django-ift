from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import AbstractUser


class Betreuer(models.Model):
    class Meta:
            verbose_name_plural = 'Betreuer'

    vorname = models.CharField(max_length=120, null=True)
    nachname = models.CharField(max_length=120, null=True)

    def __str__(self): # Python 3.3 is __str__
        return self.nachname


class MyUser(AbstractUser):

    # Username = models.CharField(max_length=40, unique=True)
    Vertragstunden = models.IntegerField(null=True)
    Vertragsstart = models.DateField(null=True)
    Vertragsende = models.DateField(null=True)
    Initstunden = models.IntegerField(default=0)
    # first_name = models.CharField(max_length=60, blank=False)



class ZeitErfassung(models.Model):
    class Meta:
            verbose_name_plural = 'Zeiterfassung'

    """In dieser Tabelle werden alle Zeiten erfasst."""

    beschreibung = models.CharField(max_length=120)
    start = models.DateTimeField()
    ende = models.DateTimeField()
    # pause = models.DurationField(null=True)
    user = models.ForeignKey(MyUser, null=True)
    betreuer = models.ForeignKey(Betreuer, null=True)
    dt = models.DurationField(null=True)
    
    timestamp = models.DateTimeField(auto_now_add=True,
                                     auto_now=False,
                                     null=True)

    # Ueberhang = models.FloatField(default=10.0)

    def __unicode__(self):
        """Convert into unicode so dass umlaute auch lesbar sind."""
        return u"%s" % self.beschreibung

    @property
    def timecalc(self):
        """Berechnet timediff."""
        return self.ende - self.start

    def save(self, *args, **kwargs):
        """Speichert das feld dt extra ab."""
        self.dt = self.timecalc
        super(ZeitErfassung, self).save(*args, **kwargs) # Call the "real" save() method.


    def get_absolute_url(self):
        return u'/thanks/' 
 
