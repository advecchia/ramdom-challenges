import unittest
import random
import math
from typing import List

MIN_VALID_NUMBER = -10**6
MAX_VALID_NUMBER = 10**6
MAX_NUMBER_LIST_SIZE = 10**6

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


# How do you implement a bucket sort algorithm?
# Solution:http://javarevisited.blogspot.sg/2017/01/bucket-sort-in-java-with-example.html
# https://en.wikipedia.org/wiki/Bucket_sort
class BucketSort(object):
    def __init__(self):
        pass

    def sort(self, numbers:List[int], bucket_size:int):
        # Validate input array
        if not numbers:
            raise ValueError('Invalid number array')

        # Validate array size
        len_numbers = len(numbers)
        if len_numbers > MAX_NUMBER_LIST_SIZE:
            raise ValueError('Invalid number array size')

        # Define the number of buckets to use
        max_bucket_number = math.floor(math.sqrt(len_numbers))
        if bucket_size > max_bucket_number:
            bucket_size = max_bucket_number
        print('Using bucket size = ' + str(bucket_size))

        # Initiate bucket list
        buckets = []
        for i in range(bucket_size):
            buckets.append([])

        # Get distribution factor - max array value
        distribution_factor = max(numbers)

        # Fill the buckets
        for number in numbers:
            if number < MIN_VALID_NUMBER or number > MAX_VALID_NUMBER:
                raise ValueError('Invalid number')

            # This math will return the bucket number, so reduced it by one to obtain the index
            index = math.floor((number * bucket_size) / distribution_factor)
            # Deal with negative value number or index overflow
            if index < 0:
                index = 0
            elif index >= bucket_size:
                index = bucket_size - 1
            buckets[index].append(number)

        # Show buckets snapshot
        print('Bucket snapshot before sorting:')
        print(buckets)

        # Sort each bucket using MergeSort and fill the output list
        merge_sort = MergeSort()
        sorted_array = []
        for bucket in buckets:
            if bucket:
                sorted_array.extend(merge_sort.sort(bucket))

        return sorted_array


def main():
    testcase = unittest.TestCase()
    algorithm = BucketSort()
    expected = [-1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 21, 32, 43, 54, 65, 76, 87, 98, 109, 110]

    print('TC1: Bucket sorting: ' + str([]) + ' Bucket size: 3')
    with testcase.assertRaises(ValueError):
        algorithm.sort([], 3)

    print('TC2: Bucket sorting: ' + str([4]) + ' Bucket size: 3')
    testcase.assertEqual(algorithm.sort([4], 3), [4])

    print('Expected below TCs: ' + str(expected))

    items = list(expected)
    random.shuffle(items)
    print('TC3 - Bucket sorting: ' + str(items) + ' Bucket size: 6')
    testcase.assertEqual(algorithm.sort(items, 6), expected)

    random.shuffle(items)
    print('TC4 - Bucket sorting: ' + str(items) + ' Bucket size: 12')
    testcase.assertEqual(algorithm.sort(items, 12), expected)

    random.shuffle(items)
    print('TC5 - Bucket sorting: ' + str(items) + ' Bucket size: 4')
    testcase.assertEqual(algorithm.sort(items, 4), expected)

    random.shuffle(items)
    print('TC6 - Bucket sorting: ' + str(items) + ' Bucket size: 5')
    testcase.assertEqual(algorithm.sort(items, 5), expected)


if __name__ == '__main__':
    main()