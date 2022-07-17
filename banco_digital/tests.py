from django.test import TestCase

class NomeTestCase(TestCase):
    
    def test_nome(self):
        nome = 'Renata'
        self.assertTrue('Renata')
