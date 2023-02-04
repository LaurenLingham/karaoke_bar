import unittest

from classes.bar import Bar
from classes.guest import Guest
from classes.song import Song
from classes.room import Room

class TestBar(unittest.TestCase):
    def setUp(self):
        self.bar = Bar("The Mic Drop", 1000.00)
        self.room = Room("Room 1", 5.00, 5)

    def test_has_name(self):
        self.assertEqual("The Mic Drop", self.bar.name)
    
    def test_has_balance(self):
        self.assertEqual(1000.00, self.bar.balance)

    def test_can_add_room(self):
        self.bar.add_room(self.room)
        self.assertEqual(1, len(self.bar.rooms))
