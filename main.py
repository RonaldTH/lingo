# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import sys
import lingowords
import logging

logging.basicConfig(level=logging.DEBUG)

# def main():
#     logging.basicConfig(level=logging.INFO)
#     lingo = lingowords.LingoWords("lingowords_en.txt")
# #     for test_word in [["oprui", "MOOOO"], ["slenk", "OOMMO"], ["anode", "OMMOM"], ["noest", "MPMOO"], ["bonen", "OPPPP"], ["wonen", "PPPPP"]]:
#     for test_word in [["oprui", "OOOOM"], ["anode", "OOOOO"], ["wijkt", "OMMOO"], ["ijzig", "MMOMO"], ["prijs", "OOPPM"]]:
#         print(lingo.show_word(test_word[0], test_word[1]))
#         lingo.process_word(test_word[0], test_word[1])
#         possible_words = lingo.find_words()
#         print("Word: ", test_word)
#         print(len(possible_words))
#         print(possible_words)

def main():
    lingo = lingowords.LingoWords("lingowords_en.txt")
#    lingo = lingowords.LingoWords("lingowords_du.txt")
    print("Play Lingo and give words with found letters.")
    possible_words = lingo.find_words()
    print(len(possible_words))
    print(possible_words)
    while lingo.word != "!":
        lingo.word = input("Word: ")
        lingo.pattern = input("Pattern: ")
        print("Word: ", lingo.show_word())
        lingo.process_word()
        possible_words = lingo.find_words()
        print(len(possible_words))
        print(possible_words)




# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
