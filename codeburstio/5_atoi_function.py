import unittest
import random
from typing import List

# Using int limit from python 2 for this toy problem
# In Python 3, there is no real limit, the container is used instead: sys.maxsize
# Equivalent to -2147483649
MIN_INTEGER = -2**31-1
# Equivalent to 2147483647
MAX_INTEGER = 2**31-1

MINUS_OPERATOR = '-'
PLUS_OPERATOR = '+'
VALID_OPERATORS = [MINUS_OPERATOR, PLUS_OPERATOR]

# How do you convert a given String into int like the atoi()?
# Solution: https://javarevisited.blogspot.com/2011/08/convert-string-to-integer-to-string.html
class Atoi(object):
    def __init__(self):
        pass

    def run(self, input_number:str):
        """ From C atoi:
            This function returns the converted integral number as an int value.
            If no valid conversion could be performed, it returns zero.
        """
        # Not a string
        if not input_number:
            return 0

        # Keep the input value untouched
        number = str(input_number)

        # empty string
        number = number.strip()
        if len(number) == 0:
            return 0

        # Verify the existence of an operator
        operator = None
        if number[0] in VALID_OPERATORS:
            operator = number[0]
            number = number[1:]

        # Verify the rest of number for only numeric characters
        if not number.isnumeric():
            return 0

        # Remove trailling zeroes
        while len(number) > 0 and number[0] == '0':
            number = number[1:]

        # Verify if the number is still valid: e.g. '0000' turn into '' is invalid;
        # have more tha 10 characters is invalid
        if not number.isnumeric() or len(number) > 10:
            return 0

        # If is needed return the operator
        result_number = int(number)
        if operator and (operator == MINUS_OPERATOR):
            result_number = -1 * result_number

        # Last validation is related to valid integer interval
        if result_number < MIN_INTEGER or result_number > MAX_INTEGER:
            return 0

        return result_number


def main():
    testcase = unittest.TestCase()
    algorithm = Atoi()

    print('TC1: "None" expected: 0')
    testcase.assertEqual(algorithm.run(None), 0)

    print('TC2: "" expected: 0')
    testcase.assertEqual(algorithm.run(''), 0)

    print('TC3: " " expected: 0')
    testcase.assertEqual(algorithm.run(' '), 0)

    print('TC4: "    " expected: 0')
    testcase.assertEqual(algorithm.run('    '), 0)

    print('TC5: "-" expected: 0')
    testcase.assertEqual(algorithm.run('-'), 0)

    print('TC6: "+" expected: 0')
    testcase.assertEqual(algorithm.run('+'), 0)

    print('TC7: "a" expected: 0')
    testcase.assertEqual(algorithm.run('a'), 0)

    print('TC8: "-a" expected: 0')
    testcase.assertEqual(algorithm.run('-a'), 0)

    print('TC9: "1-" expected: 0')
    testcase.assertEqual(algorithm.run('1-'), 0)

    print('TC10: "+a" expected: 0')
    testcase.assertEqual(algorithm.run('+a'), 0)

    print('TC11: "-2147483650" expected: 0')
    testcase.assertEqual(algorithm.run(str(MIN_INTEGER-1)), 0)

    print('TC12: "2147483648" expected: 0')
    testcase.assertEqual(algorithm.run(str(MAX_INTEGER+1)), 0)

    print('TC13: "+1" expected: 1')
    testcase.assertEqual(algorithm.run('+1'), 1)

    print('TC14: "-1" expected: -1')
    testcase.assertEqual(algorithm.run('-1'), -1)

    print('TC15: "-2147483649" expected: -2147483649')
    testcase.assertEqual(algorithm.run(str(MIN_INTEGER)), MIN_INTEGER)

    print('TC16: "2147483647" expected: 2147483647')
    testcase.assertEqual(algorithm.run(str(MAX_INTEGER)), MAX_INTEGER)

    print('TC17: "+00000000000" expected: 0')
    testcase.assertEqual(algorithm.run('+00000000000'), 0)

    print('TC18: "-00000012" expected: -12')
    testcase.assertEqual(algorithm.run('-00000012'), -12)


if __name__ == '__main__':
    main()