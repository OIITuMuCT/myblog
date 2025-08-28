import unittest
from rest_framework.test import APITestCase
from rest_framework.exceptions import ErrorDetail
from rest_framework import status
from rest_framework.authtoken.models import Token

from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User


@unittest.skip("Skipping this entire test case for now")
class BasicTests(APITestCase):
    """ Test #1 """
    def test_basic_req(self):
        """ Test the basic url path response """
        # ARRANGE-Create a URL adn expected response.

        url = '/blog/hello-world/'
        expected_data = {'msg': "hello world!"}
        # expected_data = {
        #     "detail": ErrorDetail(
        #         string="Authentication credentials were not provided.",
        #         code="not_authenticated",
        #     )
        # }

        # ACT  - Perform API call by DRF's test APIClient.
        response = self.client.get(url, format='json')
        # ASSERT - Verify the response.
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertEqual(response.data, expected_data)

class BasicTests2(APITestCase):
    def test_unauthenticated_req(self):
        url = '/blog/hello-world-2/'
        response = self.client.get(url, format='json')

        # Since user is no logged in it would get 401.
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_authenticated_req(self):
        url = '/blog/hello-world-2/'
        expected_data = {'msg': "hello world!"}
        user = User.objects.create_user(username='demouser', password='demopass')
        token, created = Token.objects.get_or_create(user=user)

        # Login the request using the HTTP header token.
        self.client.credentials(HTTP_AUTHORIZATION=f'Token {token.key}')
        response = self.client.get(url, format='json')

        # User is logged in we would get the expected 200 response code.
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, expected_data)

    def test_wrong_authenticated_req(self):
        url = '/blog/hello-world-2/'

        # Login to the request using a random wrong token.
        self.client.credentials(HTTP_AUTHORIZATION=f'Token random')
        response = self.client.get(url, format='json')

        # Request has wrong token so it would get 401.
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_force_authenticate_with_user(self):
        """ 
        Setting `.force_authenticate()` with a user forcibly authenticates.
        """
        u1 = User.objects.create_user('a1', 'a1@abc.co')
        url = '/blog/hello-world-2/'

        # Forcefully login and update request.user
        self.client.force_authenticate(user=u1)
        response = self.client.get(url)
        expected_data = {"msg": "hello world!"}
        
        # Tests work with the login user.
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, expected_data)
