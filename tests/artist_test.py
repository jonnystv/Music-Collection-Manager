import unittest
from models.artist import Artist

class TestArtist(unittest.TestCase):

    def setUp(self):
        self.artist = Artist("Barry", "Manilow", None)


    def test_artist_has_first_name(self):
        self.assertEqual("Barry", self.artist.first_name)

    
    def test_artist_has_last_name(self):
        self.assertEqual("Manilow", self.artist.last_name)


    def test_artist_has_id(self):
        self.assertEqual(None, self.artist.id)