from abc import abstractmethod, ABCMeta


class IPhoneticAlgo(metaclass=ABCMeta):
    """Implements various phonetic algorithms"""

    @abstractmethod
    def encode_word(self, word):
        """Encode word into string representation"""


class Soundex(IPhoneticAlgo):

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
