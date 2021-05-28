from typing import List


class Graph(object):
    def __init__(self, graph: list) -> None:
        super().__init__()
        if not graph or len(graph) == 0:
            raise ValueError('Not a valid graph')

        self.nodes = dict()
        for pair in graph:
            # TODO: Need test for positive integer and integer type
            if type(pair) is not tuple or len(pair) != 2 or pair[0] is None or pair[1] is None:
                raise ValueError('Not a valid edge pair')

            if pair[0] in self.nodes.keys():
                self.nodes[pair[0]].append(pair[1])
            else:
                self.nodes[pair[0]] = [pair[1]]

            if pair[1] not in self.nodes.keys():
                self.nodes[pair[1]] = []

    def contains(self, node_value):
        return node_value in self.nodes.keys()

    def get_neighbors(self, node_value) -> List:
        if node_value in self.nodes.keys():
            return self.nodes[node_value]

        raise ValueError('Searched node value is not present')