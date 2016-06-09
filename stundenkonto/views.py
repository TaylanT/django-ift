
from django.shortcuts import render, HttpResponseRedirect
from login.models import ZeitErfassung,MyUser
import datetime

# Create your views here.
def ubersicht(request):
	#zt=ZeitErfassung.objects.all()
	#current_month=datetime.now().month
	zt=ZeitErfassung.objects.filter(user__username=request.user).order_by('start')

	return render(request,'uebersicht.html',{'zt':zt})
def status(request):
	user_zeit=ZeitErfassung.objects.filter(user__username=request.user)

	summe=datetime.timedelta(0)

	for zeit in user_zeit:
		summe=summe+zeit.dt
	

	return render(request,'status.html',{'summe':summe})
  
def thanks(request):
	return render(request,'thanks.html',{})