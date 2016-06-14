
from django.shortcuts import render
from login.models import ZeitErfassung
import datetime
import locale

locale.setlocale(locale.LC_ALL, 'de_DE@euro')

# Create your views here.


def ubersicht(request):

    heute = datetime.date.today()
    aktueller_monat = heute.month
    zt = ZeitErfassung.objects.filter(user__username=request.user, start__month=aktueller_monat).order_by('start')

    return render(request, 'uebersicht.html', {'zt': zt, 'monat': heute.strftime("%B")})


def status(request):
    heute = datetime.date.today()
    aktueller_monat = heute.month

    user_zeit = ZeitErfassung.objects.filter(user__username=request.user, start__month=aktueller_monat)
    # vertrag_stunden=MyUser.objects.filter(user__username=request.user)
    summe = datetime.timedelta(0)

    for zeit in user_zeit:
        summe = summe+zeit.dtc

    summe = summe.total_seconds()/3600.0
    return render(request, 'status.html', {'summe': summe})


def thanks(request):
    return render(request, 'thanks.html', {})
