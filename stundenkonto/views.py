
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
        else:
            monat = datetime.date.today().month
        context['monat'] = monat

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
    else:
        monat = datetime.date.today().month
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
    return render(request, 'status.html', {'summe': summe, 
                                           'ueberhang': ueberhang,
                                           'monat': monat,
                                           'Vertragsstunden': MyUser.objects.get(username=request.user).Vertragstunden,
                                           'monatslist' : monatsliste,
                                           })


def thanks(request):
    return render(request, 'thanks.html', {})

