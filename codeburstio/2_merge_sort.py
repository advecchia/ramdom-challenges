import unittest
import random
from typing import List

# How is a merge sort algorithm implemented?
# Solution: http://www.java67.com/2018/03/mergesort-in-java-algorithm-example-and.html
# https://en.wikipedia.org/wiki/Merge_sort#:~:text=In%20computer%20science%2C%20merge%20sort,in%20the%20input%20and%20output.
class MergeSort(object):
    def __init__(self):
        pass

    def merge(self, left:List[int], right:List[int]):
        result = []

        # Verify and merge both sublists
        while len(left) > 0 and len(right) > 0:
            if left[0] < right[0]:
                result.append(left[0])
                left.pop(0)
            else:
                result.append(right[0])
                right.pop(0)

        # Put the rest of left on result
        if len(left) > 0:
            result.extend(left)
            left = []

        # Put the rest of right on result
        if len(right) > 0:
            result.extend(right)
            right = []

        return result

    def divide_conquer(self, elements:List[int]):
        elements_size = len(elements)
        if elements_size <= 1:
            return elements

        # Split sublists in left and right sides
        half_size = elements_size//2
        left = self.divide_conquer(elements[:half_size])
        right = self.divide_conquer(elements[half_size:])

        # Return merged results
        return self.merge(left, right)

    def sort(self, elements:List[int]):
        if not type(elements) == list:
            raise ValueError('Invalid input')

        elements_size = len(elements)
        if elements_size <= 1:
            # Self ordered for empty or one element array
            return elements

        return self.divide_conquer(elements)


def main():
    testcase = unittest.TestCase()
    algorithm = MergeSort()
    expected = [-1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 21, 32, 43, 54, 65, 76, 87, 98, 109, 110]

    print('TC1: Merge sorting: ' + str([]))
    testcase.assertEqual(algorithm.sort([]), [])

    print('TC2: Merge sorting: ' + str([4]))
    testcase.assertEqual(algorithm.sort([4]), [4])

    print('Expected below TCs: ' + str(expected))

    items = list(expected)
    random.shuffle(items)
    print('TC3 - Merge sorting: ' + str(items))
    testcase.assertEqual(algorithm.sort(items), expected)

    random.shuffle(items)
    print('TC4 - Merge sorting: ' + str(items))
    testcase.assertEqual(algorithm.sort(items), expected)

    random.shuffle(items)
    print('TC5 - Merge sorting: ' + str(items))
    testcase.assertEqual(algorithm.sort(items), expected)

    random.shuffle(items)
    print('TC6 - Merge sorting: ' + str(items))
    testcase.assertEqual(algorithm.sort(items), expected)

if __name__ == '__main__':
    main()