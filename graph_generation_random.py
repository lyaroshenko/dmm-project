from graph import Graph
from tsp import tsp_alg
from visualisation import GraphVisualization
import time

graph = Graph(20)
graph.generate_random_graph(density=0.8, weight_range=(1, 6)) # density 1 для повного графа!

graph.display_matrix()
graph.display_list()
graph.display_edges()


visualizer = GraphVisualization(graph.adjacency_list)
start_time = time.perf_counter()
(path, total) = tsp_alg(graph)
elapsed_time = time.perf_counter() - start_time

print(f'Path: {path} \n Total min cost: {total}')
print(f"Time elapsed: {(time.perf_counter() - start_time)*1000:.2f} ms")



start_time = time.perf_counter()
visualizer.visualize() # last line in code!
print(f"Visualisation took: {(time.perf_counter() - start_time)*1000:.2f} ms")