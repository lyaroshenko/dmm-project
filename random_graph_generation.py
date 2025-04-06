from graph import Graph
from visualisation import GraphVisualization
if __name__ == "__main__":
    graph = Graph(10)
    graph.generate_random_graph(density=0.3, weight_range=(1, 50))
    graph.display_matrix()
    graph.display_list()
    graph.display_edges()
    visualizer = GraphVisualization(graph.adjacency_list)
    visualizer.visualize()