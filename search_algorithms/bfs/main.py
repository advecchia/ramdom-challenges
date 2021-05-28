from domain.bfs import BFS

def main():
    root_value = 2
    input_graph = [(0, 1), (1, 2), (2, 0)]
    #input_graph = [(0, 1), (1, 0), (1, 2), (2, 1), (2, 0), (0, 2)]
    algorithm = BFS(input_graph, root_value)
    algorithm.run()

if __name__ == '__main__':
    main()