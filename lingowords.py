"""
    This class collects lingo words and can be searched
"""
import re
import logging
from colorama import Fore, Style


class LingoWords:
    """
        This class collects lingo words which can be searched upon
    """

    def __init__(self, filename):
        logging.info("Init %s", self.__module__)
        self._lingo_list: list = list()
        with open(filename, "r") as file:
            for word in file.read().split('\n'):
                if len(word) == 5 and re.search("\d", word) is None:
                    self._lingo_list.append(word.lower())
        self._position = [" "] * 5
        self._not_on_position = []
        self._match = []
        self._omit = []
        self._pattern = ""
        self.word = ""

    @property
    def pattern(self):
        return self._pattern

    @pattern.setter
    def pattern(self, value):
        if re.search("[PMO]", value.upper()) is None:
            value = ""
        self._pattern = str(value).ljust(5, "O").upper()

    def find(self, word):
        return self._lingo_list.index(word)

    def count(self):
        return len(self._lingo_list)

    def word(self, index):
        return self._lingo_list[index]

    def show_word(self):
        pmo = {'P': Fore.GREEN, 'M': Fore.YELLOW, 'O': Fore.LIGHTBLACK_EX}
        colored_return = ""
        for i in range(len(self.word)):
            colored_return += pmo[self.pattern[i]] + self.word[i]
        return colored_return + Style.RESET_ALL

    def process_word(self):
        """
            Match lingo letters.
            P gives a letter on correct position
            M matches a letter, but it's on wrong position
            O omit this letter because it's not part of the word
            Example (rapen): MrPaOpPeOn (a, e are on right pos, r is not. Omit p, o
        :return:
        """
        for p in range(len(self.word)):
            match_type = self.pattern[p]
            letter = self.word[p]
            logging.debug("Match added: %s for letter: %s", match_type, letter)
            # match on position. Place in on the variable
            if match_type == "P":
                self._position[p] = letter
                # If it's in the match list, remove it because this could be a matched letter
                if letter in self._match:
                    self._match.remove(letter)
            # match on non-position. Add it if it's not there
            elif match_type == "M":
                if letter not in self._match:
                    self._match.append(letter)
                # Store the position of the non-match. It's used in a filter
                self._not_on_position.append([letter, p])
            # letter does not exist. Put it in the omit-list
            elif match_type == "O" and letter not in self._omit:
                self._omit.append(letter)
            # at all times, if a letter is matched, remove it from the omitted list.
            if letter in self._match and letter in self._omit:
                self._omit.remove(letter)

    def find_words(self):
        """
            Build regex patterns for omitting- search- and on-position- letters
        :return: A list with words which apply to the filters
        """
        omit_pattern = ""
        match_pattern = ""
        position_pattern = ""
        not_on_position_pattern = ""
        rlist = list()

        # Add letters to the filter which all don't exist in the word (is not None)
        # Example: ^(?!.*o)^(?!.*p)^(?!.*r)^(?!.*u)
        for p in self._omit:
            omit_pattern += f"^(?!.*{p})"

        # Add letters to the filter which all do exist in the word (somewhere) (is not None)
        # Example: (i|j).*(i|j).*
        make_match_pattern = str().join([f"{item}|" for item in self._match]).removesuffix("|")
        for p in self._match:
            match_pattern += f"({make_match_pattern}).*"
        last_position = -1

        # Add letters to the non-position list. It contains pairs: the letter and the position (is None)
        for p in range(len(self._not_on_position)):
            not_on_position_pattern += f"^.{{{self._not_on_position[p][1]}}}{self._not_on_position[p][0]}|"
        not_on_position_pattern = not_on_position_pattern.removesuffix("|")
        if len(not_on_position_pattern) == 0:
            not_on_position_pattern = "!"

        # Put letters on the position in the word (is not None)
        # Example: ^.{2}i.{1}j (Starts with: ..i.j)
        for p in range(len(self._position)):
            if self._position[p] != " ":
                position_pattern += f".{{{p - last_position - 1}}}{self._position[p]}"
                last_position = p
        position_pattern = "^" + position_pattern
        logging.debug("omit_pattern: %s", omit_pattern)
        logging.debug("match_pattern: %s", match_pattern)
        logging.debug("not_on_position_pattern : %s", not_on_position_pattern)
        logging.debug("position_pattern: %s", position_pattern)
        for word in self._lingo_list:
            if (    re.search(omit_pattern, word) is not None
                    and re.search(match_pattern, word) is not None
                    and re.search(position_pattern, word) is not None
                    and re.search(not_on_position_pattern, word) is None):
                rlist.append(word)
        return rlist

    def propose_words(self):
        pass
