import unittest
import random
from typing import List

# How do you remove duplicates from an array in place?
# Solution: http://javarevisited.blogspot.com/2014/01/how-to-remove-duplicates-from-array-java-without-collection-API.html
class ArrayClean(object):
    def __init__(self):
        """ Should remove duplicates from an input array in place
        """
        pass

    def run(self, values: List[int]):
        if not values:
            return values

        len_values = len(values)
        if len_values <= 1:
            return values

        unique_values = []
        current_index = 0
        while len_values > current_index:
            if values[current_index] in unique_values:
                len_values -= 1
                current_index -= 1
                del values[current_index]
            else:
                unique_values.append(values[current_index])

            current_index += 1

        return values


def main():
    testcase = unittest.TestCase()
    algorithm = ArrayClean()
    values = [-1, 2, 2, 2, 5, 6, 7, 7, 7, 7, 21, 32, 43, 54, 54, 76, 87, 87, 109, 110]
    expected = [-1, 2, 5, 6, 7, 21, 32, 43, 54, 76, 87, 109, 110]

    print('TC1 input: ' + str(None))
    testcase.assertEqual(algorithm.run(None), None)

    print('TC2 input: ' + str([]))
    testcase.assertEqual(algorithm.run([]), [])

    print('TC3 input: ' + str([4]))
    testcase.assertEqual(algorithm.run([4]), [4])

    print('TC4 input: ' + str(values))
    testcase.assertEqual(algorithm.run(values), expected)   

    items = list(values)
    random.shuffle(items)
    print('TC4 input: ' + str(items))
    testcase.assertEqual(algorithm.run(items), list(dict.fromkeys(items)))

    random.shuffle(items)
    print('TC5 input: ' + str(items))
    testcase.assertEqual(algorithm.run(items), list(dict.fromkeys(items)))

    random.shuffle(items)
    print('TC6 input: ' + str(items))
    testcase.assertEqual(algorithm.run(items), list(dict.fromkeys(items)))

    random.shuffle(items)
    print('TC7 input: ' + str(items))
    testcase.assertEqual(algorithm.run(items), list(dict.fromkeys(items)))

    random.shuffle(items)
    print('TC8 input: ' + str(items))
    testcase.assertEqual(algorithm.run(items), list(dict.fromkeys(items)))


if __name__ == '__main__':
    main()