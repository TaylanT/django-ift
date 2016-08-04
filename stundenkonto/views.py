
from django.shortcuts import render
from django.views.generic.list import ListView
from django.shortcuts import get_object_or_404
from login.models import ZeitErfassung, MyUser
from stundenkonto.models import StatusUebersicht
import datetime
import locale
import calendar


#locale.setlocale(locale.LC_ALL, 'de_DE@euro')
locale.setlocale(locale.LC_ALL, 'deu_deu')


# Create your views here.
class UebersichView(ListView):
    """Liste fuer Uebersicht."""

    template_name = "uebersicht.html"

    def get_queryset(self, *args, **kwargs):
        """"Angepasste Queryset."""
        if(self.kwargs != {}):
            monat = self.kwargs['monat']
        else:
            monat = datetime.date.today().month
        return ZeitErfassung.objects.filter(user__username=self.request.user,
                                            start__month=monat).order_by('start')

    def get_context_data(self, **kwargs):
        """Erweitererung contexdata."""
        heute = datetime.date.today()
        jahr = heute.year
        context = super(UebersichView, self).get_context_data(**kwargs)
        #context['monat'] = heute.strftime("%B")
        if(self.kwargs != {}):
            monat = self.kwargs['monat']
            monat = int(monat)

            # Neues Datum mit eingebenen Monat geht bestimmt besser ->> #heute.replace(month = monat)
            datum = datetime.date(jahr, monat, 1)
            monat = datum.strftime("%B")
        else:
            monat =  heute.strftime("%B")
        # VerfuegbareMonate aus Statusuebersicht des Users
        monate = StatusUebersicht.objects.values_list('Monat', flat=True).filter(User=self.request.user).order_by('Monat')

        context['monate'] = monate
        context['monat'] = monat
        context['jahr'] = heute.year
        return context

def status(request):
    """Berechnung der Gesamtstunden Und Ueberhang nach Prinzip Fat Models."""
    test = StatusUebersicht()
    summe = test.berechnen(request)
    ueberhang = test.ueberhang(request)
    # summeNeu = summe/ueberhang
    return render(request, 'status.html', {'summe': summe, 
                                           'ueberhang': ueberhang,
                                           'monat': StatusUebersicht().get_aktuellermonat(),
                                           'Vertragsstunden': MyUser.objects.get(username=request.user).Vertragstunden
                                           })


def thanks(request):
    return render(request, 'thanks.html', {})

