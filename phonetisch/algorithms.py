import re
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

    def __extract_char_groups(self, word, char):
        regular_expression = char + '*' + char
        result = re.search(regular_expression, word)
        return result.group() if result is not None else None

    def __init__(self):
        self.__vowels = ['a', 'e', 'i', 'o', 'u']

        self.step_1 = lambda word: re.compile('[^a-zA-Z]').sub('', word).lower()
        self.step_2 = lambda word: word.replace('cough', 'cou2f') if word.startswith('cough') else word
        self.step_3 = lambda word: word.replace('rough', 'rou2f') if word.startswith('rough') else word
        self.step_4 = lambda word: word.replace('tough', 'tou2f') if word.startswith('tough') else word
        self.step_5 = lambda word: word.replace('enough', 'enou2f') if word.startswith('enough') else word
        self.step_6 = lambda word: word.replace('gn', '2n') if word.startswith('gn') else word
        self.step_7 = lambda word: word.replace('mb', 'm2') if word.endswith('enough') else word
        self.step_8 = lambda word: word.replace('cq', '2q').replace('ci', 'si').replace('ce', 'se').replace \
            ('cy', 'sy').replace('tch', '2ch').replace('c', 'k').replace('q', 'k').replace('x', 'k').replace \
            ('v', 'f').replace('dg', '2g').replace('tio', 'sio').replace('tia', 'sia').replace('d', 't').replace \
            ('ph', 'fh').replace('b', 'p').replace('sh', 's2').replace('z', 's')

        self.step_9 = lambda word: word.replace(word[0], 'A') if word[0] in self.__vowels else word
        self.step_10 = lambda word: word.replace('e', '3').replace('i', '3').replace('o', '3').replace('u', '3')
        self.step_11 = lambda word: word.replace('3gh3', '3kh3').replace('gh', '22').replace('g', 'k')

        self.step_12 = lambda word: word.replace(self.__extract_char_groups(word, 's'),
                                                 'S') if self.__extract_char_groups(word, 's') is not None else word
        self.step_13 = lambda word: word.replace(self.__extract_char_groups(word, 't'),
                                                 'T') if self.__extract_char_groups(word, 't') is not None else word
        self.step_14 = lambda word: word.replace(self.__extract_char_groups(word, 'p'),
                                                 'P') if self.__extract_char_groups(word, 'p') is not None else word
        self.step_15 = lambda word: word.replace(self.__extract_char_groups(word, 'k'),
                                                 'K') if self.__extract_char_groups(word, 'k') is not None else word
        self.step_16 = lambda word: word.replace(self.__extract_char_groups(word, 'f'),
                                                 'F') if self.__extract_char_groups(word, 'f') is not None else word
        self.step_17 = lambda word: word.replace(self.__extract_char_groups(word, 'm'),
                                                 'M') if self.__extract_char_groups(word, 'm') is not None else word
        self.step_18 = lambda word: word.replace(self.__extract_char_groups(word, 'n'),
                                                 'N') if self.__extract_char_groups(word, 'n') is not None else word

        self.step_19 = lambda word: word.replace('w3', 'W3').replace('wy', 'Wy').replace('wh3', 'Wh3').replace \
            ('why', 'Why').replace('w', '2')
        self.step_20 = lambda word: word.replace(word[0], 'A') if word[0] == 'h' else word
        self.step_21 = lambda word: word.replace('h', '2').replace('r3', 'R3').replace('ry', 'Ry').replace \
            ('r', '2').replace('l3', 'L3').replace('ly', 'Ly').replace('I', '2').replace('j', 'y').replace \
            ('y3', 'Y3').replace('y', '2')
        self.step_22 = lambda word: word.replace('2', '').replace('3', '')
        self.step_23 = lambda word: (word + '111111')[0:6]

        self.steps = [self.step_1, self.step_2, self.step_3, self.step_4, self.step_5, self.step_6, self.step_7,
                      self.step_8, self.step_9, self.step_10, self.step_11, self.step_12, self.step_13,
                      self.step_14, self.step_15, self.step_16, self.step_17, self.step_18, self.step_19, self.step_20,
                      self.step_21, self.step_22, self.step_23]

    def encode_word(self, word):
        pipeline = Pipeline(self.steps)
        return pipeline.execute(word)


class ColognePhonetics(PhoneticStrategy):

    def encode_word(self, word1):
        word = list(word1)
        code = ''
        if word[0] == 'X':
            code = code + '48'
        if (word[0] == 'C' and (
                word[1] == 'A' or word[1] == 'H' or word[1] == 'K' or word[1] == 'L' or word[1] == 'O' or word[
            1] == 'Q' or
                word[1] == 'U' or word[1] == 'X')):
            code = code + '4'
        if (word[0] == 'C' and (
                word[1] == 'B' or word[1] == 'C' or word[1] == 'D' or word[1] == 'E' or word[1] == 'F' or word[
            1] == 'G' or
                word[1] == 'I' or word[1] == 'J' or word[1] == 'M' or word[1] == 'N' or word[1] == 'P' or word[
                    1] == 'S' or
                word[1] == 'T' or word[1] == 'V' or word[1] == 'W' or word[1] == 'Y' or word[1] == 'Z')):
            code = code + '8'
        for i in range(0, (len(word))):

            if (word[i] == 'A' or word[i] == 'E' or word[i] == 'I' or word[i] == 'J' or word[i] == 'O' or word[
                i] == 'U' or
                    word[i] == 'Y' or word[i] == 'Ä' or word[i] == 'Ö' or word[i] == 'Ü' or word[i] == 'ß'):
                code = code + '0'
            if word[i] == 'B':
                code = code + '1'
            if word[i] == 'F' or word[i] == 'V' or word[i] == 'W':
                code = code + '3'
            if word[i] == 'G' or word[i] == 'K' or word[i] == 'Q':
                code = code + '4'
            if word[i] == 'L':
                code = code + '5'
            if word[i] == 'M' or word[i] == 'N':
                code = code + '6'
            if word[i] == 'R':
                code = code + '7'
            if word[i] == 'S' or word[i] == 'Z':
                code = code + '8'
            if word[i] == 'P':
                code = code + '1'
            if word[i] == 'P' and word[i + 1] == 'H':
                code = code + '3'
            if word[i] == 'X' and (word[i - 1] == 'C' or word[i - 1] == 'K' or word[i - 1] == 'Q'):
                code = code + '8'
            if (word[i] == 'X' and (
                    word[i - 1] == 'A' or word[i - 1] == 'B' or word[i - 1] == 'D' or word[i - 1] == 'E' or word[
                i - 1] == 'F' or word[i - 1] == 'G' or word[i - 1] == 'H' or word[i - 1] == 'I' or word[i - 1] == 'J' or
                    word[i - 1] == 'L' or word[i - 1] == 'M' or word[i - 1] == 'N' or word[i - 1] == 'O' or word[
                        i - 1] == 'P' or word[i - 1] == 'R' or word[i - 1] == 'S' or word[i - 1] == 'T' or word[
                        i - 1] == 'U' or word[i - 1] == 'V' or word[i - 1] == 'W' or word[i - 1] == 'X' or word[
                        i - 1] == 'Y' or word[i - 1] == 'Z')):
                code = code + '48'

            if word[i] == 'C' and (word[i - 1] == 'S' or word[i - 1] == 'Z'):
                code = code + '8'
            if (word[i] == 'C' and (word[i - 1] != 'S' and word[i - 1] != 'Z') and (
                    word[i + 1] == 'A' or word[i + 1] == 'H' or word[i + 1] == 'K' or word[i + 1] == 'O' or word[
                i + 1] == 'Q' or word[i + 1] == 'U' or word[i + 1] == 'X')):
                code = code + '4'

            if (word[i] == 'C' and (
                    word[i + 1] == 'B' or word[i + 1] == 'C' or word[i + 1] == 'D' or word[i + 1] == 'E' or word[
                i + 1] == 'F' or word[i + 1] == 'G' or word[i + 1] == 'I' or word[i + 1] == 'J' or word[i + 1] == 'L' or
                    word[i + 1] == 'M' or word[i + 1] == 'N' or word[i + 1] == 'P' or word[i + 1] == 'R' or word[
                        i + 1] == 'S' or word[i + 1] == 'T' or word[i + 1] == 'V' or word[i + 1] == 'W' or word[
                        i + 1] == 'Y' or word[i + 1] == 'Z')):
                code = code + '8'
            if ((word[i] == 'D' or word[i] == 'T') and i != (len(word) - 1) and (
                    word[i + 1] == 'C' or word[i + 1] == 'S' or word[i + 1] == 'Z')):
                code = code + '8'
            if ((word[i] == 'D' or word[i] == 'T') and i != (len(word) - 1) and (
                    word[i + 1] == 'A' or word[i + 1] == 'B' or word[i + 1] == 'D' or word[i + 1] == 'E' or word[
                i + 1] == 'F' or word[i + 1] == 'G' or word[i + 1] == 'H' or word[i + 1] == 'I' or word[i + 1] == 'J' or
                    word[i + 1] == 'K' or word[i + 1] == 'L' or word[i + 1] == 'M' or word[i + 1] == 'N' or word[
                        i + 1] == 'O' or word[i + 1] == 'P' or word[i + 1] == 'Q' or word[i + 1] == 'R' or word[
                        i + 1] == 'T' or word[i + 1] == 'U' or word[i + 1] == 'V' or word[i + 1] == 'W' or word[
                        i + 1] == 'X' or word[i + 1] == 'Y' or word[i + 1] == '\n')):
                code = code + '2'
        if word[len(word) - 1] == 'D' or word[len(word) - 1] == 'T':
            code = code + '2'
            print(code)

        code = code.replace('0', '')
        code1 = list(code)
        for i in range(0, (len(code1)) - 1):
            if code1[i] == code1[i + 1]:
                code1[i] = '0'
        code_final = ''.join(map(str, code1))
        code_final = code_final.replace('0', '')
        return code_final
