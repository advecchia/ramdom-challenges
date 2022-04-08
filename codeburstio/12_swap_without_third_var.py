import unittest
import random
from typing import List

MAX_INT = 10**6
MIN_INT = -10**6

# How do you swap two numbers without using the third variable?
# Solution: http://www.java67.com/2015/08/how-to-swap-two-integers-without-using.html
class SwapNumbers(object):
    def __init__(self):
        pass

    def run(self, first:int, other:int) -> List[int]:
        if (type(first) is not int) or (type(other) is not int):
            raise ValueError('Invalid input')

        if first < MIN_INT or other < MIN_INT or first > MAX_INT or other > MAX_INT:
            raise ValueError('Invalid input')

        first += other
        other = first - other
        first -= other

        return [first, other]

def main():
    testcase = unittest.TestCase()
    algorithm = SwapNumbers()

    print('TC1: (17, None)')
    with testcase.assertRaises(ValueError):
        algorithm.run(17, None)

    print('TC2: (None, 17)')
    with testcase.assertRaises(ValueError):
        algorithm.run(None, 17)

    print('TC3: (17, 10)')
    testcase.assertEqual(algorithm.run(17, 10), [10, 17])

    print('TC4: (10, 17)')
    testcase.assertEqual(algorithm.run(10, 17), [17, 10])

    print('TC5: (-10, 17)')
    testcase.assertEqual(algorithm.run(-10, 17), [17, -10])

    print('TC6: (10, -17)')
    testcase.assertEqual(algorithm.run(10, -17), [-17, 10])

    print('TC7: (1, 0)')
    testcase.assertEqual(algorithm.run(1, 0), [0, 1])

    print('TC8: (0, 1)')
    testcase.assertEqual(algorithm.run(0, 1), [1, 0])

    print('TC9: (-1, 0)')
    testcase.assertEqual(algorithm.run(-1, 0), [0, -1])

    print('TC10: (0, -1)')
    testcase.assertEqual(algorithm.run(0, -1), [-1, 0])

    print('TC11: (10**6+1, 0)')
    with testcase.assertRaises(ValueError):
        algorithm.run(10**6+1, 0)

    print('TC12: (-10**6-1, 0)')
    with testcase.assertRaises(ValueError):
        algorithm.run(-10**6-1, 0)

    print('TC13: (0, 10**6+1)')
    with testcase.assertRaises(ValueError):
        algorithm.run(0, 10**6+1)

    print('TC14: (0, -10**6-1)')
    with testcase.assertRaises(ValueError):
        algorithm.run(0, -10**6-1)

if __name__ == '__main__':
    main()