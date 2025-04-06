import networkx as nx
import matplotlib.pyplot as plt
class GraphVisualization:
    def __init__(self, adjacency_list):
        self.adjacency_list = adjacency_list
    def visualize(self):
        G = nx.Graph()
        for from_vertex, edges in self.adjacency_list.items():
            for to_vertex, weight in edges:
                G.add_edge(from_vertex, to_vertex, weight=weight)
        pos = nx.spring_layout(G)
        nx.draw(G, pos, with_labels=True, node_size=700, node_color="pink", font_size=10)
        edge_labels = nx.get_edge_attributes(G, 'weight')
        nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
        plt.title("Visualization of the Graph")
        plt.show()
