import unittest

from classes.song import Song

class TestSong(unittest.TestCase):
    def setUp(self):
        self.song = Song("Without Me", "Eminem")

    def test_song_has_title(self):
        self.assertEqual("Without Me", self.song.title)

    def test_song_has_artist(self):
        self.assertEqual("Eminem", self.song.artist)
