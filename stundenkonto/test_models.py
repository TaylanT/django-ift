from django.core.urlresolvers import reverse
from django.test import TestCase
from django.test import Client
from login.models import Betreuer, MyUser
from stundenkonto.models import StatusUebersicht

from login.models import ZeitErfassung
import pytz
import datetime




class StatusUebersichTest(TestCase):
    def setUp(self):
        self.betreuer = Betreuer.objects.create(vorname='Taylan',
                                                nachname='Tokan')
        self.user = MyUser.objects.create_user('john', 'lennon@thebeatles.com',
                                               'johnpassword')
        ZeitErfassung.objects.create(beschreibung='test1',
                                     start=datetime.datetime(2016, 1, 1, 13).replace(tzinfo=pytz.UTC),
                                     ende=datetime.datetime(2016, 1, 1, 15).replace(tzinfo=pytz.UTC),
                                     betreuer=Betreuer.objects.get(pk=1),
                                     user=MyUser.objects.get(pk=1))
        ZeitErfassung.objects.create(beschreibung='test2',
                                     start=datetime.datetime(2016, 1, 2, 13).replace(tzinfo=pytz.UTC),
                                     ende=datetime.datetime(2016, 1, 2, 15).replace(tzinfo=pytz.UTC),
                                     betreuer=Betreuer.objects.get(pk=1),
                                     user=MyUser.objects.get(pk=1))

    def test_berechnung(self):
        """Testet berechnen funktion."""
        c = Client()
        c.login(username='john', password='johnpassword')
        te = StatusUebersicht()
        self.assertEqual(te.berechnen(self, 1), 4)

    def test_berechnung_eintrag_nicht_vorhanden(self):
        """Monat umgestellt auf Februar."""
        c = Client()
        c.login(username='john', password='johnpassword')
        te = StatusUebersicht()
        self.assertEqual(te.berechnen(self, 2), 0)
