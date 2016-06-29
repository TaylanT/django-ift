
from django.shortcuts import render
from django.views.generic.list import ListView
from django.shortcuts import get_object_or_404
from login.models import ZeitErfassung
from stundenkonto.models import StatusUebersicht
import datetime
import locale
import calendar

locale.setlocale(locale.LC_ALL, 'de_DE')

# Create your views here.



class UebersichView(ListView):
    """Liste fuer Uebersicht."""


    template_name = "uebersicht.html"



    def get_queryset(self):
        heute = datetime.date.today()
        aktueller_monat = heute.month
        return ZeitErfassung.objects.filter(user__username=self.request.user,
                                            start__month=aktueller_monat).order_by('start')

    def get_context_data(self, **kwargs):
        heute = datetime.date.today()

        context = super(UebersichView, self).get_context_data(**kwargs)
        context['monat'] = heute.strftime("%B")
        return context


def status(request):
    # heute = datetime.date.today()
    # aktueller_monat = heute.month

    test = StatusUebersicht()
    summe = test.berechnen(request)
    # summe = summe + zeit.ueberhang
    return render(request, 'status.html', {'summe': summe})


def thanks(request):
    return render(request, 'thanks.html', {})

