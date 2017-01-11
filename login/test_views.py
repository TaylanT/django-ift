from django.core.urlresolvers import reverse
from django.test import TestCase
from django.test import Client
from login.models import MyUser
from login.models import Betreuer
from login.views import home
from login.models import MyUser



class home(TestCase):
    def setUp(self):
        
        self.betreuer = Betreuer.objects.create(vorname='Taylan',
                                                nachname='Tokan')

        self.client = Client()
        self.user = MyUser.objects.create_user(username="john",
                                               password="johnpassword",
                                               Vertragstunden=30,
                                               Initstunden=100)

    
   

        
    def test_homse(self):
        c = Client()
        c.login(username='john', password='johnpassword')
        form_data = {'beschreibung': 'something',
                     'start': '01.01.2016 11:00',
                     'ende': '01.01.2016 11:00',
                     'betreuer': Betreuer.objects.get(pk=1).pk}
        response = c.post('/', data=form_data)
        

        #self.assertTrue(self.Client.login(username='john',
        #                                  password='johnpassword'))




