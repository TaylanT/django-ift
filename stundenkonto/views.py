
from django.shortcuts import render
from django.views.generic.list import ListView
from django.shortcuts import get_object_or_404
from login.models import ZeitErfassung, MyUser
from stundenkonto.models import StatusUebersicht, Studenten
import datetime
import locale
import calendar

from dateutil import relativedelta
from django.core.exceptions import ObjectDoesNotExist

import operator


locale.setlocale(locale.LC_ALL, 'de_DE')


#locale.setlocale(locale.LC_ALL, 'de_DE.utf8')

#locale.setlocale(locale.LC_ALL, 'deu_deu')

#locale.setlocale(locale.LC_ALL, 'de_DE@euro')

# Class based View
class UebersichView(ListView):
    """Liste fuer Uebersicht."""

    template_name = "uebersicht.html"

    def get_queryset(self, *args, **kwargs):
        """"Angepasste Queryset."""
        if(self.kwargs != {}):
            monat = self.kwargs['monat']
            
        else:
            heute = datetime.date.today()
            monat = heute.month
        return ZeitErfassung.objects.filter(user__username=self.request.user,
                                            start__month=monat).order_by('start')

    def get_context_data(self, **kwargs):
        """Erweitererung contexdata."""
        # heute = datetime.date.today()
        context = super(UebersichView, self).get_context_data(**kwargs)
        # context['monat'] = heute.strftime("%B")
        if(self.kwargs != {}):
            monat = self.kwargs['monat']
        else:
            monat = datetime.date.today().month
        context['monat'] = datetime.date(1900, int(monat), 1).strftime('%B')

        versuch = {}
        for x in range(1, 13):
            zt = ZeitErfassung.objects.filter(user__username=self.request.user,
                                              start__month=x)
            if zt.count() > 0:
                # month = datetime.date(1900, x, 1).strftime('%B')
                versuch[x] = datetime.date(1900, x, 1).strftime('%B')
            else:
                pass
        sorted_versuch = sorted(versuch.items(), key=operator.itemgetter(0))
        context['monatslist'] = sorted_versuch
        
        return context


# Funktions-based view
def status(request, *args, **kwargs):
    """Berechnung der Gesamtstunden Und Ueberhang nach Prinzip Fat Models."""
    
    if (kwargs != {}):

        for key in kwargs:
            monat = kwargs[key]
            
    else:
        monat = datetime.date.today().month

    test = StatusUebersicht()
    summe = test.berechnen(request, monat)
    ueberhang = test.ueberhang(request, monat)
    aktueller_benutzer = MyUser.objects.get(username=request.user)

    vertragsstunden_benutzer = aktueller_benutzer.Vertragstunden
    initstunden = aktueller_benutzer.Initstunden

    # Differenz aus Vertragsdauer --> Vertragsmonate 
    # Monate werden mit Vertragsstunden multiplizert --> Gesamststunden die zu arbeiten sind (negative Zahl um abzuarbeiten)
    # Schleife ueber gearbeitete Stunden, wird auf Gesamtstunden addiert
    #print(aktueller_benutzer.Vertragsende - aktueller_benutzer.Vertragsstart) 
    r = relativedelta.relativedelta(aktueller_benutzer.Vertragsende, aktueller_benutzer.Vertragsstart)

    monateVertragsdauer = 0
    if(r.years >= 1):  
        for x in range(1,r.years + 1):
            monateVertragsdauer = monateVertragsdauer + 12
            
    monateVertragsdauer = monateVertragsdauer + r.months
    # print monateVertragsdauer, " Monate Vertrag"
    alles = monateVertragsdauer * vertragsstunden_benutzer
    # wenn tage existieren --> wird halber monat berechnet, wenn nicht ganzer monat
    if r.days:
        alles = alles + (vertragsstunden_benutzer/2)
    # print alles, " stunden zu arbeiten"
    gearbeiteteStunden = 0
    for x in range(1, 13):

        ss = test.berechnen(request, x)
        gearbeiteteStunden = gearbeiteteStunden + ss
        # hier verbesserung weil es kann auch sien dass ein ganzer kompletter Monat nicht gearebeitet worden ist. 
        #lieber ueber vertragsdauer?
    # print gearbeiteteStunden, " gearbeitete Stunden"
    gearbeiteteStunden = gearbeiteteStunden + initstunden

    # namens darstellung des Monats
    monat = int(monat)
    monat_name = datetime.date(1900, monat, 1).strftime('%B')

    versuch = {}
    for x in range(1, 13):
            zt = ZeitErfassung.objects.filter(user__username=request.user,
                                              start__month=x)
            if zt.count() > 0:
                # month = datetime.date(1900, x, 1).strftime('%B')
                versuch[x] = datetime.date(1900, x, 1).strftime('%B')
            else:
                pass

    sorted_versuch = sorted(versuch.items(), key=operator.itemgetter(0))

    return render(request, 'status.html', {'summe': summe, 
                                           'ueberhang': ueberhang,
                                           'monat': monat_name,
                                           'Vertragsstunden': MyUser.objects.get(username=request.user).Vertragstunden,
                                           'gearbeiteteStunden': gearbeiteteStunden,
                                           'gesamtstatus' : alles,
                                           'monatslist': sorted_versuch

                                           })


def thanks(request):
    return render(request, 'thanks.html', {})

