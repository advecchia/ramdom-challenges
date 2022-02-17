import unittest
import random
from typing import List

class ClassName(object):
    def __init__(self):
        pass

    def run(self):
        raise ValueError('Invalid input')

def main():
    testcase = unittest.TestCase()
    algorithm = ClassName()
    expected = None

    print('TC1: ' + str(None))
    testcase.assertEqual(algorithm.run(None), None)

if __name__ == '__main__':
    main()