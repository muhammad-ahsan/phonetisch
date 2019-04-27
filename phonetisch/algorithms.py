from abc import abstractmethod, ABCMeta

from phonetisch.utils import Pipeline


class PhoneticStrategy(metaclass=ABCMeta):
    """Implements various phonetic algorithms"""

    @abstractmethod
    def encode_word(self, word):
        """Encode word into string representation

        Parameters
        ----------
        word : string
            The word to be converted into a phonetic code according to phonetic algorithm strategy.
        Returns
        -------
        code : phonetic strategy mapping code
            Encoded string corresponding to word.
        """


class Soundex(PhoneticStrategy):

    def encode_word(self, word):
        code = word.upper()[0] + ''
        previous = '7'
        for i in range(1, len(word)):
            current = Soundex.__getCode__(word.upper()[i])
            if len(current) > 0 and current != previous:
                code += current

            previous = current
        return code

    @staticmethod
    def __getCode__(character):

        if character in ['B', 'F', 'P', 'V']:
            return '1'
        elif character in ['C',
                           'G',
                           'J',
                           'K',
                           'Q',
                           'S',
                           'X',
                           'Z']:
            return '2'
        elif character in ['D', 'T']:
            return '3'

        elif character in ['L']:
            return '4'

        elif character in ['M', 'N']:
            return '5'
        elif character in ['R']:
            return '6'
        return ''


class Caverphone(PhoneticStrategy):

    def __init__(self):
        self.step_1 = lambda word: word.replace('a', 'b')
        self.step_2 = lambda word: word.replace('b', 'c')
        self.steps = [self.step_1, self.step_2]

    def encode_word(self, word):
        pipeline = Pipeline(self.steps)
        return pipeline.execute(word)
