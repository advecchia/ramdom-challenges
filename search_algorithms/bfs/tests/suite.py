import unittest
from test_case_graph import GraphTestCase
from test_case_bfs import BFSTestCase


def build_suite():
    suite = unittest.TestSuite()
    suite.addTest(GraphTestCase('Some Graph tests'))
    suite.addTest(BFSTestCase('Some BFS tests'))
    return suite

if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    runner.run(build_suite())