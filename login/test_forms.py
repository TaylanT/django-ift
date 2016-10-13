from django.test import TestCase
from login.forms import ZeitForm, MyCustomUserForm
from login.models import Betreuer, MyUser


class Zeiterfassung_test(TestCase):

    def setUp(self):
        self.betreuer = Betreuer.objects.create(vorname='Taylan',
                                                nachname='Tokan')

    def test_forms(self):
        """Test fuer Zeiterfassung Formular."""
        betreuer_pk = Betreuer.objects.get(pk=1).pk
        form_data = {'beschreibung': 'something',
                     'start': '01.01.2016 11:00',
                     'ende': '01.01.2016 11:00',
                     'betreuer': betreuer_pk}
        form = ZeitForm(data=form_data)
        self.assertTrue(form.is_valid())

class Registrierungs_test(TestCase):

    def test_registration(self):
        """Testet die Registrierung."""
        form_data_regis = {'first_name': 'taylan',
                           'last_name': 'tokan',
                           'email': 'taylan.tokan@web.de',
                           'username': 'taylant',
                           'Vertragstunden': 20,
                           'password1': 'testooopw',
                           'password2': 'testooopw',
                           'Vertragsstart': '10.10.2016',
                           'Vertragsende': '10.10.2016'}

        form_regis = MyCustomUserForm(data=form_data_regis)
        self.assertTrue(form_regis.is_valid())
        