from django.core.urlresolvers import reverse
from django.test import TestCase
from login.models import MyUser
from django.test import Client
from stundenkonto.views import UebersichView
from login.models import ZeitErfassung


class UebersichViewTest(TestCase):
    #def login(self):


    def setUp(self):
        self.client = Client()
        self.user = MyUser.objects.create_user('john', 'lennon@thebeatles.com',
                                               'johnpassword',
                                               Vertragstunden=30,
                                               Initstunden=100)
        


    def test_login(self):
        self.assertTrue(self.client.login(username='john',
                                          password='johnpassword'))

    def test_stundenkonto_view(self):
        response = self.client.get(reverse('stundenkonto', kwargs={'monat': 7}))
        self.assertEqual(response.status_code, 200)

    # def test_status_view(self):
    #     self.client.login(username='john',
    #                       password='johnpassword')
    #     response = self.client.get(reverse('status', kwargs={'monat': 7}))
    #     self.assertEqual(response.status_code, 200)
    def test_initstunden(self):
        pass




