import unittest

from classes.guest import Guest
from classes.bar import Bar
from classes.drink import Drink
from classes.room import Room
from classes.song import Song

class TestGuest(unittest.TestCase):
    def setUp(self):
        self.song = Song("Without Me", "Eminem")
        self.guest1 = Guest("Christopher Walken", 79, 50.00, self.song)
        self.guest2 = Guest("Ricky Gervais", 58, 5.00, self.song)
        self.item = Drink("Berry Smoothie", 10.00)

    def test_has_name(self):
        self.assertEqual("Christopher Walken", self.guest1.name)

    def test_has_age(self):
        self.assertEqual(79, self.guest1.age)

    def test_has_wallet(self):
        self.assertEqual(50.00, self.guest1.wallet)

    def test_has_favourite_song(self):
        self.assertEqual(self.song, self.guest1.favourite_song)

    def test_can_afford__true(self):
        self.assertEqual(True, self.guest1.can_afford(self.item))

    def test_can_afford__false(self):
        self.assertEqual(False, self.guest2.can_afford(self.item))

    def test_can_pay_tab(self):
        self.guest1.buy_item(self.item)
        self.guest1.pay_tab()
        self.assertEqual(40.00, self.guest1.wallet)