from django import forms

from .models import ZeitErfassung, Betreuer,MyUser
from registration.forms import RegistrationForm
from registration.forms import RegistrationForm




class ZeitForm(forms.ModelForm):
	class Meta:
		model = ZeitErfassung
		fields = ['beschreibung', 'start','ende','betreuer']
		#exclude = ('user')



class MyCustomUserForm(RegistrationForm):
    class Meta:
        model = MyUser
        fields = ['username','Vertragstunden','Vertragsstart','Vertragsende']
        #fields = ['Username','Vertragstunden']