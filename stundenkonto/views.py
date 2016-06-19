
from django.shortcuts import render
from django.views.generic.list import ListView
from django.shortcuts import get_object_or_404
from login.models import ZeitErfassung
import datetime
import locale

locale.setlocale(locale.LC_ALL, 'de_DE@euro')

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
    heute = datetime.date.today()
    aktueller_monat = heute.month

    user_zeit = ZeitErfassung.objects.filter(user__username=request.user,
                                             start__month=aktueller_monat)
    ueberhangstunden = ZeitErfassung.objects.filter(user__username=request.user)
    # vertrag_stunden=MyUser.objects.filter(user__username=request.user)
    summe = datetime.timedelta(0)

    for zeit in user_zeit:
        summe = summe + zeit.ende-zeit.start

    summe = summe.total_seconds() / 3600.0
    # summe = summe + zeit.ueberhang
    return render(request, 'status.html', {'summe': summe})


def thanks(request):
    return render(request, 'thanks.html', {})
