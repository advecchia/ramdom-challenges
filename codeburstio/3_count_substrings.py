import unittest
import random
from typing import List

# How do you count the occurrence of a given character in a string?
# Solution: http://javarevisited.blogspot.sg/2012/12/how-to-count-occurrence-of-character-in-String.html
class Solution(object):
    def __init__(self):
        pass

    def count(self, word:str, occurrence:str):
        result = 0
        len_word = len(word)
        len_occurrence = len(occurrence)
        if len_word == 0 or len_occurrence == 0 or len_word < len_occurrence:
            return result

        # Executes a linear find
        for i in range(len_word - len_occurrence + 1):
            if occurrence == word[i:i + len_occurrence]:
                result += 1

        return result

    def count_python(self, word:str, occurrence:str):
        return word.count(occurrence)

def main():
    testcase = unittest.TestCase()
    algorithm = Solution()
    words = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'xyz', 'xyz', 'xyz', 'xyz']
    occurrence = 'xyz'
    expected = 4

    print('TC1: Counting: "" in: ' + str('a'))
    testcase.assertEqual(algorithm.count('a', ''), 0)

    print('TC2: Counting: "' + occurrence + '" in: ""')
    testcase.assertEqual(algorithm.count('', occurrence), 0)

    print('Expected below TCs: ' + str(expected))

    items = list(words)

    random.shuffle(items)
    word = ''.join(items)
    print('TC3: Counting: "' + occurrence + '" in: ' + word)
    testcase.assertEqual(algorithm.count(word, occurrence), expected)

    random.shuffle(items)
    word = ''.join(items)
    print('TC4: Counting: "' + occurrence + '" in: ' + word)
    testcase.assertEqual(algorithm.count(word, occurrence), expected)

    random.shuffle(items)
    word = ''.join(items)
    print('TC5: Counting: "' + occurrence + '" in: ' + word)
    testcase.assertEqual(algorithm.count(word, occurrence), expected)

    random.shuffle(items)
    word = ''.join(items)
    print('TC6: Counting: "' + occurrence + '" in: ' + word)
    testcase.assertEqual(algorithm.count(word, occurrence), expected)

    random.shuffle(items)
    word = ''.join(items)
    print('TC7: Counting: "' + occurrence + '" in: ' + word)
    testcase.assertEqual(algorithm.count(word, occurrence), expected)

if __name__ == '__main__':
    main()