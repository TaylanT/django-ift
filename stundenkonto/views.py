
from django.shortcuts import render, HttpResponseRedirect
from login.models import ZeitErfassung,MyUser
import datetime

# Create your views here.
def ubersicht(request):
	heute=datetime.date.today()
	aktueller_monat=heute.month
	zt=ZeitErfassung.objects.filter(user__username=request.user,start__month=aktueller_monat).order_by('start')

	return render(request,'uebersicht.html',{'zt':zt,'monat':heute.strftime("%B")})
def status(request):
	
	user_zeit=ZeitErfassung.objects.filter(user__username=request.user)

	summe=datetime.timedelta(0)

	for zeit in user_zeit:
		summe=summe+zeit.dt

	summe=summe.total_seconds()/3600.0
	return render(request,'status.html',{'summe':summe})
  
def thanks(request):
	return render(request,'thanks.html',{})