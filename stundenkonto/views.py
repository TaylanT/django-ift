
from django.shortcuts import render
from django.views.generic.list import ListView
from django.shortcuts import get_object_or_404
from login.models import ZeitErfassung, MyUser
from stundenkonto.models import StatusUebersicht
import datetime
import locale
import calendar



#locale.setlocale(locale.LC_ALL, 'de_DE')
locale.setlocale(locale.LC_ALL, 'deu_deu')

#locale.setlocale(locale.LC_ALL, 'de_DE@euro')


# Create your views here.
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
            context['monat'] = monatsausgabe(monat)
        else:
            context['monat'] = datetime.date.today().strftime("%B")
        

        monatsliste = []
        for x in range(1, 12):
            zt = ZeitErfassung.objects.filter(user__username=self.request.user,
                                              start__month=x)
            if zt.count() > 0:
                monatsliste.append(x)
            else:
                pass
        context['monatslist'] = monatsliste
        return context


def status(request, *args, **kwargs):
    if(kwargs != {}):
            monat = kwargs['monat']
            monatsname = monatsausgabe(monat)
    else:
        monat = datetime.date.today().month
        monatsname = datetime.date.today().strftime("%B")
    monatsliste = []
    for x in range(1, 12):
        zt = ZeitErfassung.objects.filter(user__username=request.user, start__month=x)
        if zt.count() > 0:
            monatsliste.append(x)
        else:
            pass
    """Berechnung der Gesamtstunden Und Ueberhang nach Prinzip Fat Models."""
    test = StatusUebersicht()
    summe = test.berechnen(request, monat)
    ueberhang = test.ueberhang(request, monat)
    monat = monatsausgabe(monat)
    return render(request, 'status.html', {'summe': summe, 
                                           'ueberhang': ueberhang,
                                           'monat': monatsname,
                                           'Vertragsstunden': MyUser.objects.get(username=request.user).Vertragstunden,
                                           'monatslist' : monatsliste,
                                           })


def thanks(request):
    return render(request, 'thanks.html', {})

# wollte mal eine funktion schreiben
def monatsausgabe(monat):
    if monat == "1":
        return "Januar"
    elif monat == "2":
        return "Februar"
    elif monat == "3":
        return "Maerz"
    elif monat == "4":
        return "April"
    elif monat == "5":
        return "Mai"
    elif monat == "6":
        return "Juni"
    elif monat == "7":
        return "Juli"
    elif monat == "8":
        return "August"
    elif monat == "9":
        return "September"
    elif monat == "10":
        return "Oktober"
    elif monat == "11":
        return "November"
    elif monat == "12":
        return "Dezember"
    else:
        return ""


