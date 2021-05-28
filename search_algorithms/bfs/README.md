# BFS - Breadth First Search
Given a graph, a start node and a node to find will return a binary tree used to find the node of interest.
A graph is a list of pairs (Origin, Destination), where each pair represents and edge between two nodes:

(I unidirectional) G = [(0, 1), (1, 2), (2, 0)] is equal to 0 -> 1 -> 2 -> 0

(II bidirectional) G = [(0, 1), (1, 0), (1, 2), (2, 1), (2, 0), (0, 2)] is equal to 0 <-> 1 <-> 2 <-> 0

### Run on Windows:
> python .\main.py

## Project Testing
To run the project tests you can just choose one of the below options.

### Run tests:
> python -m unittest

### Run tests with coverage:
> coverage run -m unittest

### See coverage results:
> coverage report

### Create a html coverage report (see */htmlcov/index.html):
> coverage html