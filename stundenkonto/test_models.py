from django.core.urlresolvers import reverse
from django.test import TestCase
from django.test import Client
from login.models import Betreuer, MyUser
from stundenkonto.models import StatusUebersicht
from datetime import datetime
from login.models import ZeitErfassung



class StatusUebersichTest(TestCase):
    def setUp(self):
        self.betreuer = Betreuer.objects.create(vorname='Taylan',
                                                nachname='Tokan')
        self.user = MyUser.objects.create_user('john', 'lennon@thebeatles.com',
                                               'johnpassword')
        ZeitErfassung.objects.create(beschreibung='test1',
                             start=datetime(2016, 1, 1, 13),
                             ende=datetime(2016, 1, 1, 15),
                             betreuer=Betreuer.objects.get(pk=1),
                             user = MyUser.objects.get(pk=1))
        ZeitErfassung.objects.create(beschreibung='test2',
                             start=datetime(2016, 1, 2, 13),
                             ende=datetime(2016, 1, 2, 15),
                             betreuer=Betreuer.objects.get(pk=1),
                             user = MyUser.objects.get(pk=1))
        

    def test_berechnung(self):
        c = Client()
        c.login(username='john', password='johnpassword')
        
        te=StatusUebersicht()
        
        self.assertEqual(te.berechnen(self, 1), 4)
        
