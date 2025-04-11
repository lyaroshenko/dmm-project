from graph import Graph
from tsp import tsp_alg
from visualisation import GraphVisualization

graph = Graph(5)

graph.add_edge(0, 1, 2)
graph.add_edge(0, 2, 3)
graph.add_edge(0, 3, 9)
graph.add_edge(1, 2, 4)
graph.add_edge(1, 3, 1)
graph.add_edge(1, 4, 8)
graph.add_edge(2, 3, 5)
graph.add_edge(2, 4, 2)
graph.add_edge(3, 4, 1)
graph.add_edge(4, 0, 3)

graph.display_matrix()
graph.display_list()

graph.matrix_to_list()
graph.display_list()

graph.list_to_matrix()
graph.display_matrix()

visualizer = GraphVisualization(graph.adjacency_list)
(path, total) = tsp_alg(graph)
print(f'Path: {path} \n Total min cost: {total}')




visualizer.visualize() # last line in code!