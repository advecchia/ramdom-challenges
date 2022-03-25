import unittest
import random
from typing import List

# How do you reverse an array in place in Python?
# Solution: http://javarevisited.blogspot.com/2013/03/how-to-reverse-array-in-java-int-String-array-example.html
class ReverseArray(object):
    def __init__(self):
        """ Given an array, will reverse its values position in place.
        """
        pass

    def run(self, values:List[int]):
        if not values:
            return values

        len_values = len(values)
        if len_values <= 1:
            return values

        for start in range(len_values//2):
            final = len_values - 1 - start
            aux = values[start]
            values[start] = values[final]
            values[final] = aux

        return values


def main():
    testcase = unittest.TestCase()
    algorithm = ReverseArray()
    values = [-1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 21, 32, 43, 54, 65, 76, 87, 98, 109, 110]

    print('TC1 input: ' + str(None))
    testcase.assertEqual(algorithm.run(None), None)

    print('TC2 input: ' + str([]))
    testcase.assertEqual(algorithm.run([]), [])

    print('TC3 input: ' + str([4]))
    testcase.assertEqual(algorithm.run([4]), [4])

    items = list(values)
    random.shuffle(items)
    print('TC4 input: ' + str(items))
    expected = list(items)
    expected.reverse()
    testcase.assertEqual(algorithm.run(items), expected)

    random.shuffle(items)
    print('TC5 input: ' + str(items))
    expected = list(items)
    expected.reverse()
    testcase.assertEqual(algorithm.run(items), expected)

    random.shuffle(items)
    print('TC6 input: ' + str(items))
    expected = list(items)
    expected.reverse()
    testcase.assertEqual(algorithm.run(items), expected)

    random.shuffle(items)
    print('TC7 input: ' + str(items))
    expected = list(items)
    expected.reverse()
    testcase.assertEqual(algorithm.run(items), expected)


if __name__ == '__main__':
    main()