# from django.contrib.auth.models import User
from rest_framework.test import APIClient, APITestCase
from django.urls import reverse
from .models import MyUser


# Create your tests here.

class AuthenticationTestCase(APITestCase):
    def setUp(self):
        self.user = MyUser.objects.create_user(
            "testuser", "testuser@gmail.com", "pass1234")
        self.client = APIClient()
        self.login_url = reverse('accounts:login')
        self.getuser_url = reverse('accounts:user')
        self.access_token = self.client.post(self.login_url,
                                             {'email': 'testuser@gmail.com',
                                              'password': 'pass1234'}).json()['access']

    def test_login_jwt(self):
        '''return access and refresh token'''

        credentials = {
            'email': 'testuser@gmail.com',
            'password': 'pass1234'
        }

        response = self.client.post(self.login_url, credentials)
        print(response.status_code)
        print(response.json())
        self.assertEqual(response.status_code, 200)
        self.assertTrue('access' in response.json().keys())
        self.assertTrue('refresh' in response.json().keys())

    def test_fail_login_jwt(self):
        '''dosent return tokens if we use bad credentials'''

        credentials = {
            'email': 'testuser@gmail.com',
            'password': 'pass1234fake'
        }

        response = self.client.post(self.login_url, credentials)
        print(response.status_code)
        self.assertEqual(response.status_code, 401)

    def test_get_user_data(self):
        '''return data of authenticated user with access token'''

        self.client.credentials(
            HTTP_AUTHORIZATION='Bearer ' + self.access_token)

        response = self.client.get(self.getuser_url)
        print(response.status_code)
        print(response.json())
        self.assertEqual(response.status_code, 200)
        # self.assertTrue('id' in response.json().keys())
        # self.assertTrue('first_name' in response.json().keys())
        # self.assertTrue('last_name' in response.json().keys())
        self.assertTrue('username' in response.json().keys())
        self.assertTrue('email' in response.json().keys())
        self.assertTrue('password' in response.json().keys())
