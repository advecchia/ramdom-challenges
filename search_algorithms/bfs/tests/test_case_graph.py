import unittest
from domain.graph import Graph

class GraphTestCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_should_fail_to_create_a_graph_with_none(self):
        """Should fail to create a node with none value
        """
        self.assertRaises(ValueError, Graph, None)

    def test_should_fail_to_create_a_graph_with_empty_value(self):
        """Should fail to create a graph with empty value
        """
        self.assertRaises(ValueError, Graph, [])

    def test_should_fail_to_create_a_graph_without_tuple_content(self):
        """Should fail to create a graph without tuple content
        """
        self.assertRaises(ValueError, Graph, [[]])

    def test_should_fail_to_create_a_graph_with_wrong_tuple_size(self):
        """Should fail to create a graph with wrong tuple size
        """
        self.assertRaises(ValueError, Graph, [(0)])

    def test_should_fail_to_create_a_graph_with_wrong_tuple_first_value(self):
        """Should fail to create a graph with wrong tuple first value
        """
        self.assertRaises(ValueError, Graph, [(None, 0)])

    def test_should_fail_to_create_a_graph_with_wrong_tuple_second_value(self):
        """Should fail to create a graph with wrong tuple second value
        """
        self.assertRaises(ValueError, Graph, [(0, None)])

    def test_should_create_a_valid_graph(self):
        """Should create a valid graph
        """
        input_graph = [(0,1)]
        graph = Graph(input_graph)
        self.assertIsNotNone(graph)

    def test_should_create_a_valid_graph_with_more_nodes(self):
        """Should create a valid graph with more nodes
        """
        input_graph = [(0,1),(0,2),(1,3)]
        graph = Graph(input_graph)
        self.assertIsNotNone(graph)

    def test_graph_should_have_a_node(self):
        """Graph should have a node
        """
        input_graph = [(0,1)]
        graph = Graph(input_graph)
        self.assertTrue(graph.contains(0))

    def test_graph_should_not_have_a_node(self):
        """Graph should not have a node
        """
        input_graph = [(0,1)]
        graph = Graph(input_graph)
        self.assertFalse(graph.contains(3))

    def test_should_fail_to_retrieve_neighbors_with_invalid_node(self):
        """Should fail to retrieve neighbors with invalid node
        """
        input_graph = [(0,1)]
        graph = Graph(input_graph)
        self.assertRaises(ValueError, graph.get_neighbors, 3)

    def test_should_retrieve_neighbors_from_graph(self):
        """Should retrieve neighbors from graph
        """
        input_graph = [(0,1)]
        graph = Graph(input_graph)
        self.assertEqual(graph.get_neighbors(0), [1])