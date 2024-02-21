from django.test import TestCase
from restaurant.models import Menu


class MenuTest(TestCase):
    def test_get_item(self):
        item = Menu.objects.create(menu_id=2, title="IceCream", price=80, inventory=100)
        self.assertEqual(item.__str__(), "IceCream : 80")