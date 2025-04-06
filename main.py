from graph import Graph
from visualisation import GraphVisualization
if __name__ == "__main__":
    graph = Graph(5)

    graph.add_edge(0, 1, 10)
    graph.add_edge(1, 2, 15)
    graph.add_edge(2, 3, 20)
    graph.add_edge(3, 4, 25)
    graph.add_edge(4, 0, 30)

    graph.display_matrix()
    graph.display_list()

    graph.matrix_to_list()
    graph.display_list()

    graph.list_to_matrix()
    graph.display_matrix()

    visualizer = GraphVisualization(graph.adjacency_list)
    visualizer.visualize()