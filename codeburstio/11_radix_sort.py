import unittest
import random
import math
from typing import List

MIN_VALID_NUMBER = 0
MAX_VALID_NUMBER = 10**6
MAX_NUMBER_LIST_SIZE = 10**6
BUCKET_SIZE = 10

# How is a radix sort algorithm implemented?
# https://en.wikipedia.org/wiki/Radix_sort
# Solution: http://www.java67.com/2018/03/how-to-implement-radix-sort-in-java.html
class RadixSort(object):
    def __init__(self):
        """ Sort lexicographic data, by the distribution of 
            information along buckets, using their radix.
            This implementation will evaluate only positive 
            numbers.
            This algorithm runs like as a counting sort with multiple iterations.
        """
        pass

    def discover_bucket_number_MSD(self, number:int, current_pos:int, max_number_pos:int) -> int:
        # Convert to string
        word = str(number).zfill(max_number_pos)

        # Use list comprehension to obtain the bucket position
        return int(word[current_pos])

    def discover_bucket_number_LSD(self, number:int, current_pos:int) -> int:
        # Convert to string
        word = str(number)

        if current_pos >= len(word):
            return 0

        # Use list comprehension to obtain the bucket position
        return int(word[len(word) - 1 - current_pos])

    def get_max_number_length(self, numbers:List[int]) -> int:
        numbers_length = []
        for number in numbers:
            if number < MIN_VALID_NUMBER or number > MAX_VALID_NUMBER:
                raise ValueError('Invalid number')

            numbers_length.append(len(str(number)))
        return max(numbers_length)

    def sortLSD(self, numbers:List[int]) -> List[int]:
        """ Sort using Least Significant Digit approach
        """
        if not type(numbers) == list:
            raise ValueError('Invalid number array size')

        numbers_len = len(numbers)
        if numbers_len > MAX_NUMBER_LIST_SIZE:
            raise ValueError('Invalid number array size')

        # Self ordered for empty or one element array
        if numbers_len <= 1:
            return numbers

        # Obtain the length of the longest number to use as digit iterations, e.g. 789 will return 3, 173214 will return 6.
        max_number_length = self.get_max_number_length(numbers)

        for current_pos in range(max_number_length):
            # Creates the count array list to keep the histogram buckets for input array
            count_array = [0] * BUCKET_SIZE

            # Creates the output array list to keep the sorted array
            output_array = [None] * numbers_len

            # Build an histogram for input array
            for i in range(numbers_len):
                number = numbers[i]
                bucket_number = self.discover_bucket_number_LSD(number, current_pos)
                count_array[bucket_number] += 1

            # Performs a prefix sum to determine the position for each key
            for i in range(1, BUCKET_SIZE):
                count_array[i] += count_array[i - 1]

            # Rearrange items using the input array from a reverse order
            # Use -1 as final value for range because so it will consider position zero
            for i in range(numbers_len - 1, -1, -1):
                number = numbers[i]
                bucket_number = self.discover_bucket_number_LSD(number, current_pos)
                count_array[bucket_number] -= 1
                output_array[count_array[bucket_number]] = number

            numbers = list(output_array)

        return numbers

    def sortMSD_auxilary(self, numbers:List[int], current_pos:int, max_number_pos:int, need_recursion:bool) -> List[int]:
        # Stop the recursion when reach a position greater than the longest string length
        if current_pos > max_number_pos:
            return numbers

        output_array = []

        if current_pos == 0 or need_recursion:
            # Creates the bucket array list to keep the buckets for input array
            bucket_array = []
            for i in range(BUCKET_SIZE):
                bucket_array.append([])

            # Fill each bucket with corresponding values making first ordenation
            for i in range(len(numbers)):
                number = numbers[i]
                bucket_number = self.discover_bucket_number_MSD(number, current_pos, max_number_pos)
                bucket_array[bucket_number].append(number)

            # Remove empty buckets that will not be necessary
            for bucket in bucket_array:
                if bucket:
                    output_array.append(bucket)

            # Run for the next position
            return self.sortMSD_auxilary(list(output_array), current_pos+1, max_number_pos, False)

        else:
            # Run for each bucket after the first iteration
            for number in numbers:
                """ We can see three possible values after bucket evaluation: 
                    1. A number at its final position
                    2. A number that is unique in its bucket and could be extracted to keep its final position
                    3. A list with multiple values that need to be evaluated using buckets again
                """
                if type(number) == int:
                    output_array += [number]

                elif type(number) == list:
                    if len(number) == 1:
                        output_array += number

                    else:
                        output_array += self.sortMSD_auxilary(list(number), current_pos, max_number_pos, True)

            return output_array

    def sortMSD(self, numbers:List[int]) -> List[int]:
        """ Sort using Most Significant Digit approach
        """
        if not type(numbers) == list:
            raise ValueError('Invalid number array size')

        numbers_len = len(numbers)
        if numbers_len > MAX_NUMBER_LIST_SIZE:
            raise ValueError('Invalid number array size')

        # Self ordered for empty or one element array
        if numbers_len <= 1:
            return numbers

        # Obtain the length of the longest number to use as digit iterations, e.g. 789 will return 3, 173214 will return 6.
        max_number_length = self.get_max_number_length(numbers)

        # Use a recursive approach to deal with the problem
        return self.sortMSD_auxilary(list(numbers), 0, max_number_length, True)


def main():
    testcase = unittest.TestCase()
    algorithm = RadixSort()
    expected = [10, 12, 30, 45, 100, 739]

    print('Radix Sorting Algorithm LSD approach')
    print('TC1: sorting: "" ')
    with testcase.assertRaises(ValueError):
        algorithm.sortLSD('')

    print('TC2: sorting: ' + str([]))
    testcase.assertEqual(algorithm.sortLSD([]), [])

    print('TC3: sorting: ' + str([4]))
    testcase.assertEqual(algorithm.sortLSD([4]), [4])

    print('Expected below TCs: ' + str(expected))

    items = list(expected)
    random.shuffle(items)
    print('TC4 - sorting: ' + str(items))
    testcase.assertEqual(algorithm.sortLSD(items), expected)

    random.shuffle(items)
    print('TC5 - sorting: ' + str(items))
    testcase.assertEqual(algorithm.sortLSD(items), expected)

    random.shuffle(items)
    print('TC6 - sorting: ' + str(items))
    testcase.assertEqual(algorithm.sortLSD(items), expected)

    random.shuffle(items)
    print('TC7 - sorting: ' + str(items))
    testcase.assertEqual(algorithm.sortLSD(items), expected)

    print('Radix Sorting Algorithm MSD approach')
    print('TC1: sorting: "" ')
    with testcase.assertRaises(ValueError):
        algorithm.sortMSD('')

    print('TC2: sorting: ' + str([]))
    testcase.assertEqual(algorithm.sortMSD([]), [])

    print('TC3: sorting: ' + str([4]))
    testcase.assertEqual(algorithm.sortMSD([4]), [4])

    expected = [2, 24, 25, 45, 66, 75, 170, 802]
    print('Expected below TCs: ' + str(expected))

    items = list(expected)
    random.shuffle(items)
    print('TC4 - sorting: ' + str(items))
    testcase.assertEqual(algorithm.sortMSD(items), expected)

    random.shuffle(items)
    print('TC5 - sorting: ' + str(items))
    testcase.assertEqual(algorithm.sortMSD(items), expected)

    random.shuffle(items)
    print('TC6 - sorting: ' + str(items))
    testcase.assertEqual(algorithm.sortMSD(items), expected)

    random.shuffle(items)
    print('TC7 - sorting: ' + str(items))
    testcase.assertEqual(algorithm.sortMSD(items), expected)

if __name__ == '__main__':
    main()