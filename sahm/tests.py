from django.test import TestCase
from django.contrib.auth.models import User
from django.test.client import Client

class CadastrarMonitorTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create(first_name='Paulo Henrique', username='20159022998', email='paulo@gmail.com', password='admin1')

    def test_first_name_vazio(self):
        self.user.first_name = ""
        self.assertFalse(self.user.first_name)

    def test_username_vazio(self):
        self.assertNotEqual(self.user.username, "")

    def test_email_vazio(self):
        self.assertNotEqual(self.user.email, "")

    def test_password_vazio(self):
        self.assertNotEqual(self.user.password, "")

    def test_username_com_menos_de_11_caracteres(self):
        self.assertNotEqual(len(self.user.username) < 11, True)

    def test_password_com_menos_de_6_caracteres(self):
        self.assertNotEqual(len(self.user.password) < 6, True)

    def test_email_sem_arroba(self):
        self.assertNotEqual(self.user.email.count('@') == 0, True)

    def test_email_sem_ponto_com(self):
        self.assertNotEqual(self.user.email.count('.com') == 0, True)

    def test_cadastro_monitor(self):
        response = self.client.get('/cadastro/')
        self.assertEqual(response.status_code, 200)

    """def test_cadastrar_monitor_sucesso(self):
        data = {'first_name': 'Paulo', 'username': '20159024998', 'email': 'paulo@outlook.com', 'password': 'admin1234'}
        response = self.client.post('/cadastro/', data)
        self.assertNotEqual(data.first_name, "")"""
