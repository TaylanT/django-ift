
from django.shortcuts import render, HttpResponseRedirect
from login.models import ZeitErfassung
from datetime import datetime

# Create your views here.
def ubersicht(request):
	#zt=ZeitErfassung.objects.all()
	#current_month=datetime.now().month
	zt=ZeitErfassung.objects.filter(user__username=request.user).order_by('start')

	return render(request,'uebersicht.html',{'zt':zt})
def status(request):
	return render(request,'status.html',{})
   