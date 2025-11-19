from rest_framework.test import APITestCase
from rest_framework import status
from .models import Customer, Sushi
from decimal import Decimal

# Create your tests here.
class SushiTests(APITestCase):
    URL = "/api/sushis"

    def setUp(self):
        Sushi.objects.create(name="One Sushi", price=Decimal("5.00"))

    def test_list_sushis(self):
        response = self.client.get(self.URL)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Sushi.objects.count(), 1)
        self.assertEqual(response.data["results"][0]["name"], "One Sushi")
        self.assertEqual(Decimal(response.data["results"][0]["price"]), Decimal("5.00"))
    
    def test_get_sushi(self):
        response = self.client.get(self.URL + "/1")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["name"], "One Sushi")
        self.assertEqual(Decimal(response.data["price"]), Decimal("5.00"))

    def test_create_sushi(self):
        data = {"name": "Another Sushi", "price": Decimal("3.50")}
        response = self.client.post(self.URL, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Sushi.objects.count(), 2)
        self.assertEqual(response.data["name"], "Another Sushi")
        self.assertEqual(Decimal(response.data["price"]), Decimal("3.50"))
    
    def test_update_sushi(self):
        data = {"name": "Updated Sushi", "price": Decimal("7.25")}
        response = self.client.put(self.URL + "/1", data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Decimal(response.data["price"]), Decimal("7.25"))
    
    def test_delete_sushi(self):
        response = self.client.delete(self.URL + "/1")
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Sushi.objects.count(), 0)
    
    def test_get_nonexistent_sushi(self):
        response = self.client.get(self.URL + "/2")
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
    
    def test_create_bad_sushi(self):
        data = {"name": "Another Sushi", "price": Decimal("-3.50")}
        response = self.client.post(self.URL, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


class CustomerTests(APITestCase):
    URL = "/api/customers"
    
    def setUp(self):
        Customer.objects.create(
            name="John Doe",
            email="john.doe@gmail.com", 
            phone="+1234567890", 
            address="123 Main St, Anytown, USA"
        )

    def test_list_customers(self):
        response = self.client.get(self.URL)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Customer.objects.count(), 1)
        self.assertEqual(response.data["results"][0]["name"], "John Doe")
        self.assertEqual(response.data["results"][0]["email"], "john.doe@gmail.com")
        self.assertEqual(response.data["results"][0]["phone"], "+1234567890")
        self.assertEqual(response.data["results"][0]["address"], "123 Main St, Anytown, USA")
    
    def test_get_customer(self):
        response = self.client.get(self.URL + "/1")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["name"], "John Doe")
        self.assertEqual(response.data["email"], "john.doe@gmail.com")
        self.assertEqual(response.data["phone"], "+1234567890")
        self.assertEqual(response.data["address"], "123 Main St, Anytown, USA")

    def test_create_customer(self):
        data = {
            "name": "Jane Doe", 
            "email": "jane.doe@example.com", 
            "phone": "+12025550114", 
            "address": "128 Main St, Anytown, USA"
        }
        response = self.client.post(self.URL, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Customer.objects.count(), 2)
        self.assertEqual(response.data["name"], "Jane Doe")
        self.assertEqual(response.data["email"], "jane.doe@example.com")
        self.assertEqual(response.data["phone"], "+12025550114")
        self.assertEqual(response.data["address"], "128 Main St, Anytown, USA")
    
    def test_update_customer(self):
        data = {
            "name": "Jane Doe", 
            "email": "jane.doe@gmail.com", 
            "phone": "+12025550113", 
            "address": "128 Main St, Anytown, USA"
        }
        response = self.client.put(self.URL + "/1", data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["name"], "Jane Doe")
        self.assertEqual(response.data["email"], "jane.doe@gmail.com")
        self.assertEqual(response.data["phone"], "+12025550113")
        self.assertEqual(response.data["address"], "128 Main St, Anytown, USA")
    
    def test_delete_customer(self):
        response = self.client.delete(self.URL + "/1")
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Customer.objects.count(), 0)
    
    def test_get_nonexistent_customer(self):
        response = self.client.get(self.URL + "/2")
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
    
    def test_create_bad_customer(self):
        data = {
            "email": "jane.doe@example.com", 
            "phone": "12",
            "address": "128 Main St, Anytown, USA"
        }
        response = self.client.post(self.URL, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
