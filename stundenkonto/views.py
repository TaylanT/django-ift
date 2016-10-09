
from django.shortcuts import render
from django.views.generic.list import ListView
from django.db.models import F, FloatField, Sum
from django.shortcuts import get_object_or_404
from login.models import ZeitErfassung, MyUser
from stundenkonto.models import StatusUebersicht
import datetime
import locale
import calendar

locale.setlocale(locale.LC_ALL, 'de_DE')

# locale.setlocale(locale.LC_ALL, 'de_DE.utf8')

# locale.setlocale(locale.LC_ALL, 'de_DE@euro')

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
        for x in range(1, 12):
            zt = ZeitErfassung.objects.filter(user__username=self.request.user,
                                              start__month=x)
            if zt.count() > 0:
                # month = datetime.date(1900, x, 1).strftime('%B')
                versuch[x] = datetime.date(1900, x, 1).strftime('%B')
            else:
                pass
        context['monatslist'] = versuch
        
        return context


# Funktions-based view
def status(request, *args, **kwargs):
    """Berechnung der Gesamtstunden Und Ueberhang nach Prinzip Fat Models."""

    for key in kwargs:
        monat = kwargs[key]
    monat = int(monat)
    test = StatusUebersicht()
    summe = test.berechnen(request, monat)
    ueberhang = test.ueberhang(request, monat)
    
    aktueller_benutzer = MyUser.objects.get(username=request.user)

    alles = ZeitErfassung.objects.filter(user__username=request.user, 
                                        start__lt=datetime.datetime(2016, monat+1,1)).aggregate(test=Sum(F('dt')))
    # test = ZeitErfassung.objects.filter(user__username='taylan',)
    alles = alles['test'].total_seconds() / 3600
    
    vs = monat - aktueller_benutzer.Vertragsstart.month + 1
    
    print monat
    
    suml = alles - vs * aktueller_benutzer.Vertragstunden


    # namens darstellung des Monats
    
    monat_name = datetime.date(1900, monat, 1).strftime('%B')

    versuch = {}
    for x in range(1, 12):
            zt = ZeitErfassung.objects.filter(user__username=request.user,
                                              start__month=x)
            if zt.count() > 0:
                # month = datetime.date(1900, x, 1).strftime('%B')
                versuch[x] = datetime.date(1900, x, 1).strftime('%B')
            else:
                pass
    return render(request, 'status.html', {'summe': summe, 
                                           'ueberhang': ueberhang,
                                           'monat': monat_name,
                                           'Vertragsstunden': MyUser.objects.get(username=request.user).Vertragstunden,
                                           'gesamtstatus': suml,
                                           'monatslist': versuch
                                           })


def thanks(request):
    return render(request, 'thanks.html', {})

