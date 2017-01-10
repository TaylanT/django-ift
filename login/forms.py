from django import forms

from .models import ZeitErfassung, MyUser
from registration.forms import RegistrationForm


class ZeitForm(forms.ModelForm):
    """Zeiterfassungsformular."""
    class Meta:
        model = ZeitErfassung
        fields = ['beschreibung', 'start', 'ende', 'betreuer']


class MyCustomUserForm(RegistrationForm):
    """Registrierungs Formular."""

    class Meta:
        model = MyUser
        fields = ['first_name', 'last_name', 'username', 'Vertragstunden',
                  'Vertragsstart', 'Vertragsende', 'email']
        REQUIRED_FIELDS = ['first_name']


class EmailForm(forms.ModelForm):
    """Zeiterfassungsformular."""
    class Meta:
        model = MyUser
        fields = ['email']
        