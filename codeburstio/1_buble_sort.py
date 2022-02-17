import unittest
import random
from typing import List

# How is a bubble sort algorithm implemented?
# Solution: http://javarevisited.blogspot.sg/2014/08/bubble-sort-algorithm-in-java-with.html#axzz5ArdIFI7y
class BubleSort(object):
    def __init__(self):
        pass

    def sort(self, elements:List[int]):
        if not type(elements) == list:
            raise ValueError('Invalid input list')

        elements_size = len(elements)
        if elements_size <= 1:
            # Self ordered for empty or one element array
            return elements

        for i in range(elements_size - 1):
            # After each round the smallest element will be positioned on the left position
            for j in range(i + 1, elements_size):
                # Will raise exception for non int values
                if elements[j] < elements[i]:
                    # swap element
                    temp = elements[i]
                    elements[i] = elements[j]
                    elements[j] = temp

        return elements

def main():
    testcase = unittest.TestCase()
    algorithm = BubleSort()
    expected = [-1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 21, 32, 43, 54, 65, 76, 87, 98, 109, 110]

    print('TC1 - Buble sorting: ' + str([]))
    testcase.assertEqual(algorithm.sort([]), [])

    print('TC2 - Buble sorting: ' + str([4]))
    testcase.assertEqual(algorithm.sort([4]), [4])

    print('Expected below TCs: ' + str(expected))

    items = list(expected)
    random.shuffle(items)
    print('TC3 - Buble sorting: ' + str(items))
    testcase.assertEqual(algorithm.sort(items), expected)

    random.shuffle(items)
    print('TC4 - Buble sorting: ' + str(items))
    testcase.assertEqual(algorithm.sort(items), expected)

    random.shuffle(items)
    print('TC5 - Buble sorting: ' + str(items))
    testcase.assertEqual(algorithm.sort(items), expected)

    random.shuffle(items)
    print('TC6 - Buble sorting: ' + str(items))
    testcase.assertEqual(algorithm.sort(items), expected)


if __name__ == '__main__':
    main()