import unittest

from classes.drink import Drink

class TestDrink(unittest.TestCase):
    def setUp(self):
        self.drink = Drink("French Martini", 7.00)

    def test_drink_has_name(self):
        self.assertEqual("French Martini", self.drink.name)

    def test_drink_has_price(self):
        self.assertEqual(7.00, self.drink.price)
