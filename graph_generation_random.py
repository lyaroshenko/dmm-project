from graph import Graph
from tsp import tsp_alg
from visualisation import GraphVisualization
graph = Graph(5)
graph.generate_random_graph(density=1, weight_range=(1, 6)) # density 1 для полного графа!

graph.display_matrix()
graph.display_list()
graph.display_edges()


visualizer = GraphVisualization(graph.adjacency_list)
(path, total) = tsp_alg(graph)

print(f'Path: {path} \n Total min cost: {total}')



visualizer.visualize() # last line in code!