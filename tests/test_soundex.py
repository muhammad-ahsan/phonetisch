import unittest

from phonetisch import soundex

class TestSoundex(unittest.TestCase):

    def test_encode(self):
        assert soundex.encode_word("Example") == soundex.encode_word("Ekzampul")
