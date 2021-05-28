from domain.bfs import BFS
import unittest

class BFSTestCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_should_fail_to_construct_bfs_with_invalid_root_node(self):
        """Should fail to construct bfs with invalid root node
        """
        self.assertRaises(ValueError, BFS, [(0,1)], 3)

    def test_should_construct_bfs_with_valid_root_node(self):
        """Should construct bfs with valid root node
        """
        input_graph = [(0,1)]
        input_node = 0
        algorithm = BFS(input_graph, input_node)
        self.assertIsNotNone(algorithm)

    def test_should_run_bfs(self):
        """Should run bfs
        """
        input_graph = [(0, 1), (1, 2), (2, 0)]
        input_node = 0
        trace = [0, 1, 2]
        algorithm = BFS(input_graph, input_node)
        self.assertEqual(algorithm.run(), trace)