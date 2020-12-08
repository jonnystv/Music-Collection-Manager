import unittest
from models.album import Album

class TestAlbum(unittest.TestCase):
    def setUp(self):
        self.album = Album("Computer World", "Electronic", "Kraftwerk", None)


    def test_album_has_title(self):
        self.assertEqual("Computer World", self.album.album_title)


    def test_album_has_genre(self):
        self.assertEqual("Electronic", self.album.album_genre)


    def test_album_has_artist(self):
        self.assertEqual("Kraftwerk", self.album.album_artist)


    def test_album_has_id(self):
        self.assertEqual(None, self.album.id)