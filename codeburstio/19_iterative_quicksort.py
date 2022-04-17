import unittest
import random
from typing import List

# How is an iterative quicksort algorithm implemented?
# Solution: http://javarevisited.blogspot.sg/2016/09/iterative-quicksort-example-in-java-without-recursion.html#axzz5ArdIFI7y
class IterativeQuicksort(object):
    def __init__(self):
        pass

    def partition(self, elements:List[int], start:int, end:int):
        smaller_index = start - 1
        current_value = elements[end]
        for pointer in range(start, end):
            if elements[pointer] <= current_value:
                smaller_index += 1
                elements[smaller_index], elements[pointer] = elements[pointer], elements[smaller_index]

        elements[smaller_index + 1], elements[end] = elements[end], elements[smaller_index + 1]
        return smaller_index + 1

    def sort(self, elements:List[int]):
        if type(elements) is not list:
            raise ValueError('Invalid input')

        elements_size = len(elements)
        if elements_size <= 1:
            return elements

        # Build an auxiliary stack to keep position of elements that will need to change
        start = 0
        elements_size -= 1
        stack = [0] * (elements_size - start + 1)

        # Start value for top stack position
        top = 0
        stack[top] = start
        top = top + 1
        stack[top] = elements_size

        # Iterates while the stack is not empty
        while top >= 0:
            elements_size = stack[top]
            top = top - 1
            start = stack[top]
            top = top - 1

            # Obtains a pivot position
            pivot = self.partition(elements, start, elements_size)

            # Stack elements on pivot left side
            if pivot - 1 > start:
                top = top + 1
                stack[top] = start
                top = top + 1
                stack[top] = elements_size - 1

            # Stack elements on pivot right side
            if pivot + 1 < elements_size:
                top = top + 1
                stack[top] = pivot + 1
                top = top + 1
                stack[top] = elements_size

        return elements


def main():
    testcase = unittest.TestCase()
    algorithm = IterativeQuicksort()
    expected = [-1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 21, 32, 43, 54, 65, 76, 87, 98, 109, 110]

    print('TC1: ' + str(None))
    with testcase.assertRaises(ValueError):
        testcase.assertEqual(algorithm.sort(None), None)

    print('TC2: [3]')
    testcase.assertEqual(algorithm.sort([3]), [3])

    items = list(expected)
    print('Expected result for below test cases: ' + str(expected))

    random.shuffle(items)
    print('TC3 - sorting: ' + str(items))
    testcase.assertEqual(algorithm.sort(items), expected)

    random.shuffle(items)
    print('TC4 - sorting: ' + str(items))
    testcase.assertEqual(algorithm.sort(items), expected)

    random.shuffle(items)
    print('TC5 - sorting: ' + str(items))
    testcase.assertEqual(algorithm.sort(items), expected)

    random.shuffle(items)
    print('TC6 - sorting: ' + str(items))
    testcase.assertEqual(algorithm.sort(items), expected)

    random.shuffle(items)
    print('TC7 - sorting: ' + str(items))
    testcase.assertEqual(algorithm.sort(items), expected)

if __name__ == '__main__':
    main()