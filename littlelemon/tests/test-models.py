from django.test import TestCase
from restaurant.models import Menu

class MenuItemTest(TestCase):
    def test_get_item(self):
        # Creating an instance of your Menu model
        item = Menu.objects.create(title="IceCream", price=80.00, inventory=100) 

        # Asserting if the string representation of the item matches the expected value.
        # It should match my __str__ method's output exactly: "Title - $Price"
        # Since price is DecimalField, it will render with two decimal places by default,
        self.assertEqual(str(item), "IceCream - $80.00")