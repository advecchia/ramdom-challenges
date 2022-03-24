import unittest
import random
from typing import List

MIN_VALID_NUMBER = 0
MAX_VALID_NUMBER = 10**6
MAX_NUMBER_LIST_SIZE = 10**6

# How do you implement a counting sort algorithm?
# Solution: http://www.java67.com/2017/06/counting-sort-in-java-example.html
# https://pt.wikipedia.org/wiki/Counting_sort
class CountingSort(object):
    def __init__(self):
        """ This version of CoutingSort only works for positive integers.
        """
        pass

    def sort(self, numbers:List[int]):
        if not type(numbers) == list:
            raise ValueError('Invalid number array size')

        numbers_len = len(numbers)
        if numbers_len > MAX_NUMBER_LIST_SIZE:
            raise ValueError('Invalid number array size')

        if numbers_len <= 1:
            # Self ordered for empty or one element array
            return numbers

        # Know as k value, it is the greater number from input array
        max_value = max(numbers)

        # Create count array to keep the number with their key
        # The effect of this math is an array of the size (plus one) of the greatest number on input array filled with zeroes
        count_array = [0] * (max_value + 1)
        output_array = [None] * numbers_len

        # Build an histogram for input array
        for i in range(numbers_len):
            number = numbers[i]
            if number < MIN_VALID_NUMBER or number > MAX_VALID_NUMBER:
                raise ValueError('Invalid number')

            count_array[number] += 1

        # Performs a prefix sum to determine the position for each key
        for i in range(1, max_value + 1):
            count_array[i] += count_array[i - 1]

        # Rearrange items using the input array from a reverse order
        # Use -1 as final value for range because it ignores the last value, so stop on zero
        for i in range(numbers_len - 1, -1, -1):
            number = numbers[i]
            count_array[number] -= 1
            output_array[count_array[number]] = number

        return output_array


def main():
    testcase = unittest.TestCase()
    algorithm = CountingSort()
    expected = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 21, 32, 43, 54, 65, 76, 87, 98, 109, 110]

    print('TC1: Counting sorting: ' + str([]))
    testcase.assertEqual(algorithm.sort([]), [])

    print('TC2: Counting sorting: ' + str([4]))
    testcase.assertEqual(algorithm.sort([4]), [4])

    print('Expected below TCs: ' + str(expected))

    items = list(expected)
    random.shuffle(items)
    print('TC3 - Counting sorting: ' + str(items))
    testcase.assertEqual(algorithm.sort(items), expected)

    random.shuffle(items)
    print('TC4 - Counting sorting: ' + str(items))
    testcase.assertEqual(algorithm.sort(items), expected)

    random.shuffle(items)
    print('TC5 - Counting sorting: ' + str(items))
    testcase.assertEqual(algorithm.sort(items), expected)

    random.shuffle(items)
    print('TC6 - Counting sorting: ' + str(items))
    testcase.assertEqual(algorithm.sort(items), expected)


if __name__ == '__main__':
    main()