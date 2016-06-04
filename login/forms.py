from django import forms

from .models import SignUp, ZeitErfassung

class SignUpForm(forms.ModelForm):
	class Meta:
		model = SignUp
		fields = ['full_name', 'email']

class ZeitForm(forms.ModelForm):
	class Meta:
		model = ZeitErfassung
		fields = ['beschreibung', 'start','ende']
		#exclude = ('user')