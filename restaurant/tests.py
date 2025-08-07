from django.test import TestCase
from .models import Menu

# Create your tests here.
class MenuItemTest(TestCase):
    def setUp(self):
        Menu.objects.create(Title="Spaghetti",Price=12,Inventory=2)
        Menu.objects.create(Title="Burger",Price=10,Inventory=4)
        Menu.objects.create(Title="Spaghetti",Price=11,Inventory=8)
        Menu.objects.create(Title="Burger",Price=22,Inventory=4)
        Menu.objects.create(Title="Salad",Price=52,Inventory=5)
        self.item = Menu.objects.all()

    def test_str_method(self):
        for menu_item in self.item:
            itemstr = str(menu_item)
            self.assertEqual(itemstr,f'{menu_item.Title} : {menu_item.Price}AED')

    def test_price_is_positive(self):
        for menu_item in self.item:
            self.assertGreaterEqual(menu_item.Price,0)

    def test_inventory_is_positive(self):
        for menu_item in self.item:
            self.assertGreaterEqual(menu_item.Inventory,0)