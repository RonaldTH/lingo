"""
    This class collects lingo words and can be searched
"""
import re


class LingoWords:
    def __init__(self, filename):
        self._lingo_list: list = list()
        with open(filename, "r") as file:
            for word in file.read().split('\n'):
                if len(word) == 5 and re.search("\d", word) is None:
                    self._lingo_list.append(word.lower())

    def find(self, word):
        return self._lingo_list.index(word)

    def count(self):
        return len(self._lingo_list)

    def word(self, index):
        return self._lingo_list[index]

    def omit_letters(self, pattern):
        rlist = list()
        search_pattern = ""
        for p in pattern:
            search_pattern += "^(?!.*" + p + ")"
        for word in self._lingo_list:
            if re.search(search_pattern, word) is not None:
                rlist.append(word)
        return rlist

    def match_letters(self, pattern):
        """
            Match lingo letters.
            P gives a letter on correct position
            M matches a letter, but it's on wrong position
            O omit this letter because it's not part of the word
            Example (rapen): MrPaOpPeOn (a, e are on right pos, r is not. Omit p, o
        :param pattern:
        :return:
        """
        rlist = list()
        search_pattern = ""x
        for p in pattern:
            search_pattern += "^(?!.*" + p + ")"
        for word in self._lingo_list:
            if re.search(search_pattern, word) is not None:
                rlist.append(word)
        return rlist



