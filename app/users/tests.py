from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.test import APITestCase
from model_bakery import baker


class UserTestCase(APITestCase):
    def setUp(self) -> None:
        self.users = baker.make('auth.User', _quantity=3)


    def test_should_list(self):
        response = self.client.get('/api/users', format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        for user_response, user in zip(response.data, self.users):

            self.assertEqual(user_response['id'], user.id)
            self.assertEqual(user_response['username'], user.username)

        self.fail()
