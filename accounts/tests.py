from rest_framework.test import APIClient, APITestCase
from django.urls import reverse
from .models import User


# Create your tests here.

class AuthenticationTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            "testuser", "testuser@gmail.com", "pass1234")
        self.client = APIClient()
        self.login_url = reverse('accounts:login')
        self.getuser_url = reverse('accounts:user')

    def test_login_jwt(self):
        ''' access and refresh token'''
        credentials = {
            'email': 'testuser@gmail.com',
            'password': 'pass1234'
        }

        response = self.client.post(self.login_url, credentials)
        print(response.status_code)
        print(response.json())
        print(credentials)
        self.assertEqual(response.status_code, 200)
        self.assertTrue('access' in response.json().keys())
        self.assertTrue('refresh' in response.json().keys())
