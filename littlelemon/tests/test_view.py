from django.test import TestCase, Client
from django.urls import reverse
from rest_framework import status
from restaurant.models import Menu # Import your Menu model
from restaurant.serializers import MenuSerializer # Import your MenuSerializer

class MenuViewTest(TestCase):
    def setUp(self):
        # Create a few test instances of the Menu model
        self.client = Client() # Initialize a test client
        Menu.objects.create(title="Pizza", price=15.00, inventory=50)
        Menu.objects.create(title="Burger", price=12.50, inventory=75)
        Menu.objects.create(title="Salad", price=8.00, inventory=100)

    def test_getall(self):
        # Geting all Menu objects created in setUp
        menu_items = Menu.objects.all()
        # Serialize the expected data
        serializer = MenuSerializer(menu_items, many=True)
        expected_data = serializer.data

        # Making a GET request to the Menu API endpoint
        # 'menu-items' is a url name.

        response = self.client.get(reverse('menu-list')) 

        # Assertions
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, expected_data)
