
from django.shortcuts import render, HttpResponseRedirect
from login.models import ZeitErfassung,MyUser
import datetime
import locale
import calendar

locale.setlocale(locale.LC_ALL, 'deu_deu')

# Create your views here.
def ubersicht(request):
	heute=datetime.date.today()
	aktueller_monat=heute.month
	zt=ZeitErfassung.objects.filter(user__username=request.user,start__month=aktueller_monat).order_by('start')

	return render(request,'uebersicht.html',{'zt':zt,'monat':heute.strftime("%B")})

def status(request):
	heute=datetime.date.today()
	aktueller_monat=heute.month
	
	#vertragsstunden und stunden aus dem letzten monat speichern
	vertragstunden = MyUser.objects.get(username=request.user).Vertragstunden
	stundenLetzterMonat = MyUser.objects.get(username=request.user).StundenLetzterMonat

	user_zeit=ZeitErfassung.objects.filter(user__username=request.user,start__month=aktueller_monat)
	#vertrag_stunden=MyUser.objects.filter(user__username=request.user)
	summe=datetime.timedelta(0)

	for zeit in user_zeit:
		summe=summe+zeit.dt

	summe=summe.total_seconds()/3600.0


	#animation fuer geleistete stundenanzahl
	prozent = (summe / vertragstunden) * 100

	#info bei plusstunden
	ueberstunden = summe - vertragstunden

	#monatsende wann und wo ausfuehren?
	monatsende = calendar.monthrange(heute.year, heute.month)[1]
	
	if(heute.day == monatsende):
		aktuellerUser = MyUser.objects.get(username=request.user)
		
		aktuellerUser.StundenLetzterMonat += summe
		aktuellerUser.save()

	return render(request,'status.html',{'summe':summe, 'vertragstunden':vertragstunden, 'prozent':prozent, 
		'stundenLetzterMonat':stundenLetzterMonat, 'monat':heute.strftime("%B"), 'ueberstunden':ueberstunden})
  
def thanks(request):
	return render(request,'thanks.html',{})
