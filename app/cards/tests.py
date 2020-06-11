from django.test import TestCase

# Create your tests here.
from model_bakery import baker
from munch import Munch
from rest_framework import status
from rest_framework.test import APITestCase

from cards.models import Card


class CardTestCase(APITestCase):
    def setUp(self):
        self.card = baker.make(Card, _quantity=2)
        self.users = baker.make('auth.User', _quantity=1)

    def test_should_list(self):
        self.client.force_authenticate(user=self.users[0])
        response = self.client.get('/api/card/')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        print(response.data)
        for card_response, card in zip(response.data['results'], self.card[::-1]):
            card_response = Munch(card_response)
            self.assertEqual(card_response.id, card.id)
            self.assertEqual(card_response.no, card.no)

    def test_should_create(self):
        data = {'no': 0}
        user = self.users[0]
        self.client.force_authenticate(user=user)
        response = self.client.post('/api/card/', data=data)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        card_response = Munch(response.data)
        self.assertEqual(card_response.no, data['no'])
        self.assertEqual(card_response.user, user.id)

    def test_should_retrive(self):
        card = self.card[0]
        self.client.force_authenticate(user=self.users[0])
        response = self.client.get(f'/api/card/{card.id}/')

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        card_response = Munch(response.data)
        self.assertTrue(card_response.id)
        self.assertFalse(card_response.user)
        self.assertEqual(card_response.no, 0)
        self.fail()




        # self.client.force_authenticate(user=self.users[0])
        # prev_no = self.card[0].no

