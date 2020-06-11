from django.contrib.auth.models import User
from munch import Munch
from rest_framework import status
from rest_framework.test import APITestCase
from model_bakery import baker


class UserTestCase(APITestCase):
    def setUp(self) -> None:
        self.users = baker.make('auth.User', _quantity=3)

    def test_should_list(self):
        # 전역에 인증된 유저만 접근하도록 하였기 떄문에
        self.client.force_authenticate(user=self.users[0])

        response = self.client.get('/api/users')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        print(response.data)
        for user_response, user in zip(response.data['results'], self.users[::-1]):
            user_response = Munch(user_response)
            self.assertEqual(user_response.id, user.id)
            self.assertEqual(user_response.username, user.username)

    def test_should_create(self):
        data = {'username': "abc", "password": "1111"}
        response = self.client.post('/api/users', data=data)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        user_response = Munch(response.data)
        self.assertTrue(user_response.id)
        self.assertEqual(user_response.username, data['username'])
        # 전부 다 에러가 발생하지 않는다면, 초록생 테두리가 터미널 창에 나타난다.

        #
        #
        # # fail을 강제하는 이유는 실패한 유저를 따로 빼기 위함이다.
        # # return 값이 self.fail이라면 올바르게 테스트가 되고 있는 것
        # self.fail()

    def test_should_get(self):
        user = self.users[0]
        self.client.force_authenticate(user=user)
        response = self.client.get(f'/api/users/{user.id}')

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        user_response = Munch(response.data)
        self.assertTrue(user_response.id)
        self.assertEqual(user_response.username, user.username)

    def test_should_update(self):
        user = self.users[0]
        prev_email = user.email

        data = {'email': "test@naver.com"}
        self.client.force_authenticate(user=user)
        response = self.client.patch(f'/api/users/{user.id}', data=data)
        print(response)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        user_response = Munch(response.data)
        self.assertTrue(user_response.id)

        self.assertNotEqual(user_response.email, prev_email)
        # self.assertEqual(user_response.username, data['username'])

        # self.fail()

    def test_should_delete(self):
        user = baker.make('auth.User')
        self.client.force_authenticate(user=user)
        # user = self.users[0]

        response = self.client.delete(f'/api/users/{user.id}')

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(User.objects.filter(pk=user.id).count(), 0)
        self.assertFalse(User.objects.filter(id=user.id).exists())

    # def test(self):
    #     self.client.force_authenticate(user=self.users[0])
    #     self.client.get('/api/users/fastcampus')
    #
    #     self.fail()
