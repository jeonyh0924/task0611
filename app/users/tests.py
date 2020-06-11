from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.test import APITestCase
from model_bakery import baker


class UserTestCase(APITestCase):
    def setUp(self) -> None:
        self.user = baker.make('auth.User', _quantity=3)


    def test_should_list(self):
        response = self.client.get('/api/users', format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        user = response.data[0]
        print(user)
        self.assertEqual(user['id'], self.user.id)
        self.assertEqual(user['username'], self.user.username)

        self.fail()
