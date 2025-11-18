from rest_framework.test import APITestCase
from rest_framework import status
from .models import Sushi
from decimal import Decimal

# Create your tests here.
class SushiTests(APITestCase):
    URL = "/api/sushis"

    def setUp(self):
        Sushi.objects.create(name="One Sushi", price=Decimal("5.00"))

    def test_list_sushis(self):
        response = self.client.get(self.URL)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["results"][0]["name"], "One Sushi")
        self.assertEqual(Decimal(response.data["results"][0]["price"]), Decimal("5.00"))

    def test_create_sushi(self):
        data = {"name": "Another Sushi", "price": Decimal("3.50")}
        response = self.client.post(self.URL, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Sushi.objects.count(), 2)
        self.assertEqual(response.data["name"], "Another Sushi")
        self.assertEqual(Decimal(response.data["price"]), Decimal("3.50"))
