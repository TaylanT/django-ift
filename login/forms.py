from django import forms

from .models import ZeitErfassung, Betreuer


class ZeitForm(forms.ModelForm):
	class Meta:
		model = ZeitErfassung
		fields = ['beschreibung', 'start','ende','betreuer']
		#exclude = ('user')