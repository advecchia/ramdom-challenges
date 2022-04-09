import unittest
import random
from typing import List

class Point(object):
    def __init__(self, x:int, y:int):
        if type(x) is not int:
            raise ValueError('Invalid coordinate x')

        if type(y) is not int:
            raise ValueError('Invalid coordinate y')

        self.x = x
        self.y = y


class Rectangle(object):
    def __init__(self, topLeftPoint:Point, bottomRightPoint:Point):
        if type(topLeftPoint) is not Point:
            raise ValueError('Invalid point topLeftPoint')

        if type(bottomRightPoint) is not Point:
            raise ValueError('Invalid point bottomRightPoint')

        self.topLeftPoint = topLeftPoint
        self.bottomRightPoint = bottomRightPoint


# How do you check if two rectangles overlap with each other?
# Solution: http://javarevisited.blogspot.sg/2016/10/how-to-check-if-two-rectangle-overlap-in-java-algorithm.html
class RectanglesOverlap(object):
    def __init__(self):
        pass

    def isOverlapping(self, rectangle1: Rectangle, rectangle2: Rectangle) -> bool:
        """ The solution takes in account that when there is no overlapping
            the rectangles (A and B) will be in four possible positions:
                1: A is over B
                2: A is bellow B
                3: A is at left of B
                3: A is at right of B
        """
        if type(rectangle1) is not Rectangle:
            raise ValueError('Invalid input rectangle1')

        if type(rectangle2) is not Rectangle:
            raise ValueError('Invalid input rectangle2')

        if (rectangle1.topLeftPoint.x > rectangle2.bottomRightPoint.x) or (rectangle1.bottomRightPoint.x < rectangle2.topLeftPoint.x) or (rectangle1.topLeftPoint.y < rectangle2.bottomRightPoint.y) or (rectangle1.bottomRightPoint.y > rectangle2.topLeftPoint.y):
            return False

        return True

def main():
    testcase = unittest.TestCase()
    algorithm = RectanglesOverlap()

    print('TC1: A rectangle None')
    with testcase.assertRaises(ValueError):
        algorithm.isOverlapping(None, None)

    print('TC2: B rectangle None')
    with testcase.assertRaises(ValueError):
        algorithm.isOverlapping(Rectangle(Point(0,0), Point(0, 0)), None)

    print('TC3: A Point topLeft None')
    with testcase.assertRaises(ValueError):
        algorithm.isOverlapping(Rectangle(None, Point(0, 0)), Rectangle(Point(0,0), Point(0, 0)))

    print('TC4: A Point bottomRight None')
    with testcase.assertRaises(ValueError):
        algorithm.isOverlapping(Rectangle(Point(0, 0), None), Rectangle(Point(0,0), Point(0, 0)))

    print('TC5: A Point coordinate x None')
    with testcase.assertRaises(ValueError):
        algorithm.isOverlapping(Rectangle(Point(0, 0), Point(None, 0)), Rectangle(Point(0,0), Point(0, 0)))

    print('TC6: A Point coordinate y None')
    with testcase.assertRaises(ValueError):
        algorithm.isOverlapping(Rectangle(Point(0, 0), Point(0, None)), Rectangle(Point(0,0), Point(0, 0)))

    print('TC7: overlapping')
    a_rectangle = Rectangle(Point(0, 2), Point(2, 0))
    b_rectangle = Rectangle(Point(1, 1), Point(3, -1))
    testcase.assertEqual(algorithm.isOverlapping(a_rectangle, b_rectangle), True)

    print('TC8: A is over B')
    a_rectangle = Rectangle(Point(3, 6), Point(4, 5))
    b_rectangle = Rectangle(Point(3, 4), Point(4, 3))
    testcase.assertEqual(algorithm.isOverlapping(a_rectangle, b_rectangle), False)

    print('TC9: A is bellow B')
    a_rectangle = Rectangle(Point(3, 2), Point(4, 1))
    b_rectangle = Rectangle(Point(3, 4), Point(4, 3))
    testcase.assertEqual(algorithm.isOverlapping(a_rectangle, b_rectangle), False)

    print('TC10: A is at left of B')
    a_rectangle = Rectangle(Point(1, 4), Point(2, 3))
    b_rectangle = Rectangle(Point(3, 4), Point(4, 3))
    testcase.assertEqual(algorithm.isOverlapping(a_rectangle, b_rectangle), False)

    print('TC11: A is at right of B')
    a_rectangle = Rectangle(Point(5, 4), Point(6, 3))
    b_rectangle = Rectangle(Point(3, 4), Point(4, 3))
    testcase.assertEqual(algorithm.isOverlapping(a_rectangle, b_rectangle), False)


if __name__ == '__main__':
    main()