from django.core import mail
from django.test import TestCase

class SubscribePostValid(TestCase):
    def setUp(self):
        data = dict(name='Guilherme Augusto Maas', cpf='12345678901', email='guilherme.maas@gmail.com', phone='47-33998767')
        self.resp = self.client.post('/inscricao/', data)
        self.email = mail.outbox[0]

    def test_subscription_email_subject(self):
        expect = 'Confirmacao de inscricao'

        self.assertEqual(expect, self.email.subject)

    def test_subscription_email_from(self):
        expect = 'contato@eventex.com.br'

        self.assertEqual(expect, self.email.from_email)

    def test_subscription_email_to(self):
        expect = ['contato@eventex.com.br', 'guilherme.maas@gmail.com']

        self.assertEqual(expect, self.email.to)

    def test_subscription_email_body(self):
        contents = [
            'Guilherme Augusto Maas',
            '12345678901',
            'guilherme.maas@gmail.com',
            '47-33998767'
        ]
        for content in contents:
            with self.subTest():
                self.assertIn(content, self.email.body)
