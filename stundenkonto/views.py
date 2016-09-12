
from django.shortcuts import render
from django.views.generic.list import ListView
from django.shortcuts import get_object_or_404
from login.models import ZeitErfassung, MyUser
from stundenkonto.models import StatusUebersicht
import datetime
import locale
import calendar



# locale.setlocale(locale.LC_ALL, 'de_DE')
locale.setlocale(locale.LC_ALL, 'de_DE.utf8')

#locale.setlocale(locale.LC_ALL, 'de_DE@euro')


# Class based View
class UebersichView(ListView):
    """Liste fuer Uebersicht."""

    template_name = "uebersicht.html"

    def get_queryset(self, *args, **kwargs):
        """"Angepasste Queryset."""
        if(self.kwargs != {}):
            monat = self.kwargs['monat']
            print(monat)
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
        context['monat'] = monat

        versuch = {}
        namensliste = []
        for x in range(1, 12):
            zt = ZeitErfassung.objects.filter(user__username=self.request.user,
                                              start__month=x)
            if zt.count() > 0:
                # month = datetime.date(1900, x, 1).strftime('%B')
                versuch[x]=datetime.date(1900, x, 1).strftime('%B')
                
                
            else:
                pass
        context['monatslist'] = versuch
        
        return context


# Funktions-based view
def status(request, *args, **kwargs):
    """Berechnung der Gesamtstunden Und Ueberhang nach Prinzip Fat Models."""
    print 'bin drinne'
    if (kwargs != {}):

        for key in kwargs:
            monat = kwargs[key]
            print monat
    else:
        monat = datetime.date.today().month

    print monat
    test = StatusUebersicht()
    summe = test.berechnen(request, monat)
    print summe
    ueberhang = test.ueberhang(request, monat)
    alles=0
    aktueller_benutzer = MyUser.objects.get(username=request.user)

    Vertragsstunden_benutzer = aktueller_benutzer.Vertragstunden
    initstunden = aktueller_benutzer.Initstunden
    for x in range(1, 12):
        
        
        ss = test.berechnen(request, x)
        ab = Vertragsstunden_benutzer - ss
        # hier verbesserung weil es kann auch sien dass ein ganzer kompletter Monat nicht gearebeitet worden ist. lieber ueber vertragsdauer?
        if ab != Vertragsstunden_benutzer:
            alles = alles + ab
        else:
            pass

    alles=alles+initstunden

    print alles
    # namens darstellung des Monats
    
    monat=int(monat)
    monat_name = datetime.date(1900, monat, 1).strftime('%B')

    print monat_name

    # summeNeu = summe/ueberhang
    return render(request, 'status.html', {'summe': summe, 
                                           'ueberhang': ueberhang,
                                           'monat': monat_name,
                                           'Vertragsstunden': MyUser.objects.get(username=request.user).Vertragstunden,
                                           'gesamtstatus' : alles
                                           })


def thanks(request):
    return render(request, 'thanks.html', {})

