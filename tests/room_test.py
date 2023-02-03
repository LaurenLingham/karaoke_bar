import unittest

from classes.room import Room
from classes.guest import Guest
from classes.bar import Bar

class TestRoom(unittest.TestCase):
    def setUp(self):
        self.room1 = Room("Room 1", 7.50, 10)
        self.room2 = Room("Room 2", 5.00, 10)
        self.guest1 = Guest("Christopher Walken", 79, 50.00, "Without Me")
        self.bar = Bar("The Mic Drop", 1000.00)

    def test_has_name(self):
        self.assertEqual("Room 1", self.room1.name)

    def test_has_max_capacity(self):
        self.assertEqual(10, self.room1.capacity)

    def test_has_current_capacity(self):
        self.assertEqual(0, self.room1.head_count)

    def test_can_check_in_guest__True(self):
        self.room1.check_in_guest(self.guest1)
        self.assertEqual(1, self.room1.head_count)

    def test_can_check_in_guest__False(self):
        self.room2.head_count = 10
        self.room2.check_in_guest(self.guest1)
        self.assertEqual(10, self.room2.head_count)

    def test_can_check_out_guest(self):
        self.room1.head_count = 4
        self.room1.check_in_guest(self.guest1)
        self.room1.check_out_guest(self.guest1, self.bar)
        self.assertEqual(4, self.room1.head_count)