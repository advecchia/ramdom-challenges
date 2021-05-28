from typing import List
from domain.graph import Graph

class BFS(object):
    def __init__(self, input_graph: list, input_node: int) -> None:
        super().__init__()
        self.root = input_node
        self.graph = Graph(input_graph)

        if not self.graph.contains(self.root):
            raise ValueError('Root node not found in input graph')

    def run(self) -> List:
        trace = []
        queue = [self.root]
        visited = [self.root]

        while queue:
            visiting = queue.pop(0)
            trace.append(visiting)
            print(visiting, end = ' ')
            for neighbor in self.graph.get_neighbors(visiting):
                if neighbor not in visited:
                    visited.append(neighbor)
                    queue.append(neighbor)

        return trace