from django.test import TestCase
from login.forms import ZeitForm
from login.models import Betreuer


class MyTests(TestCase):

    def setUp(self):
        self.betreuer = Betreuer.objects.create(vorname='Taylan',
                                                nachname='Tokan')
    def test_forms(self):
        betreuer_pk = Betreuer.objects.get(pk=1).pk
        form_data = {'beschreibung': 'something',
                     'start': '01.01.2016 11:00',
                     'ende': '01.01.2016 11:00',
                     'betreuer': betreuer_pk}
        form = ZeitForm(data=form_data)
        self.assertTrue(form.is_valid())
        