from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from .models import Registration


class RegistrationAPITests(APITestCase):
    def setUp(self):
        self.list_url = reverse('name-list')  # basename is still 'name' from your router

    def test_list_empty(self):
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, [])

    def test_create_record(self):
        payload = {"username": "testuser"}
        response = self.client.post(self.list_url, payload, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Registration.objects.count(), 1)

    def test_retrieve_record(self):
        obj = Registration.objects.create(username="sampleuser")
        url = reverse('name-detail', args=[obj.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_record(self):
        obj = Registration.objects.create(username="deleteme")
        url = reverse('name-detail', args=[obj.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Registration.objects.count(), 0)