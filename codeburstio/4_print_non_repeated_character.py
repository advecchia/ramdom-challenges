import unittest
import random
from typing import List

# How do you print the first non-repeated character from a string?
# Solution: http://javarevisited.blogspot.sg/2014/03/3-ways-to-find-first-non-repeated-character-String-programming-problem.html
class FindChar(object):
    def __init__(self):
        pass

    def run(self, word:str):
        if not word:
            return ''

        word = word.strip()
        len_word = len(word)
        # Basic case, empty or non repeated character
        if len_word <= 1:
            return word

        # To solve this we will need to look up all the chars in the input word
        # We will do that un only one passage over the word string
        duplicated = []
        unique = []
        for char in list(word):
            # We will ignore already saw char to reduce the growth of the auxiliar list duplicated
            if (char not in duplicated):
                if (char in unique):
                    # Char already saw
                    unique.remove(char)
                    duplicated.append(char)
                else:
                    # New char
                    unique.append(char)

        if len(unique) > 0:
            # First appearence of non repeated char
            return unique[0]
        else:
            return ''


def main():
    testcase = unittest.TestCase()
    algorithm = FindChar()

    print('TC1: "' + str(None) + '" expected: ""')
    testcase.assertEqual(algorithm.run(None), '')

    print('TC2: "" expected: ""')
    testcase.assertEqual(algorithm.run(''), '')

    print('TC3: "aa" expected: ""')
    testcase.assertEqual(algorithm.run('aa'), '')

    print('TC4: "b" expected: "b"')
    testcase.assertEqual(algorithm.run('b'), 'b')

    print('TC5: "' + str('swiss') + '" expected: "w"')
    testcase.assertEqual(algorithm.run('swiss'), 'w')

    print('TC6: "' + str('hello') + '" expected: "h"')
    testcase.assertEqual(algorithm.run('hello'), 'h')

    print('TC7: "' + str('abcdefghijklmnopqrstuqponmlkjihgfedcba') + '" expected: "r"')
    testcase.assertEqual(algorithm.run('abcdefghijklmnopqrstuqponmlkjihgfedcba'), 'r')

if __name__ == '__main__':
    main()