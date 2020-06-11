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
        self.users = baker.make('auth.User', _quantity=3)

    def test_should_list(self):
        self.client.force_authenticate(user=self.users[0])
        response = self.client.get('/api/card')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        print(response.data)
        for card_response, card in zip(response.data['results'], self.card):
            card_response = Munch(card_response)
            self.assertEqual(card_response.id, card.id)
            self.assertEqual(card_response.no, card.no)

