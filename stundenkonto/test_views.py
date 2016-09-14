from django.test import TestCase
from django.test import Client

from login.models import MyUser

class UebersichTest(TestCase):
    def setUp(self):
        self.c = Client()
        MyUser.objects.create_user(username='ulal',
                              email='asdf@.com',
                              password='hansi',
                              Vertragstunden=30)
    def test_login(self):
        
        self.assertTrue(self.c.login(username='ulal',
                                     password='hansi'))
    def test_
