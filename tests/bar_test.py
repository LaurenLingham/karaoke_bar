import unittest

from classes.bar import Bar
from classes.guest import Guest
from classes.song import Song

class TestBar(unittest.TestCase):
    def setUp(self):
        self.bar = Bar("The Mic Drop", 1000.00)

    def test_has_name(self):
        self.assertEqual("The Mic Drop", self.bar.name)
    
    def test_has_balance(self):
        self.assertEqual(1000.00, self.bar.balance)
