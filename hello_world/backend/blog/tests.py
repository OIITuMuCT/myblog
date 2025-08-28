from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework.exceptions import ErrorDetail
from rest_framework import status

class BasicTests(APITestCase):
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
