import unittest

from classes.guest import Guest
from classes.bar import Bar
from classes.drink import Drink
from classes.room import Room
from classes.song import Song

class TestGuest(unittest.TestCase):
    def setUp(self):
        self.song = Song("Without Me", "Eminem")
        self.guest = Guest("Christopher Walken", 79, 50.00, self.song)

    def test_has_name(self):
        self.assertEqual("Christopher Walken", self.guest.name)

    def test_has_age(self):
        self.assertEqual(79, self.guest.age)

    def test_has_wallet(self):
        self.assertEqual(50.00, self.guest.wallet)

    def test_has_favourite_song(self):
        self.assertEqual(self.song, self.guest.favourite_song)

    def test_can_afford__true(self):
        pass

    def test_can_afford__false(self):
        pass
