import unittest

from phonetisch.soundex.Soundex import Soundex


class TestSoundex(unittest.TestCase):
    def test_encode(self):
        assert Soundex.encode("Example") == Soundex.encode("Ekzampul")
