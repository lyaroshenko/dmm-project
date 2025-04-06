import random
class Graph:
    def __init__(self, vertex_count):
        self.vertex_count = vertex_count
        self.adjacency_matrix = [[0] * vertex_count for _ in range(vertex_count)]
        self.adjacency_list = {i: [] for i in range(vertex_count)}

    def add_edge(self, from_vertex, to_vertex, weight):
        self.adjacency_matrix[from_vertex][to_vertex] = weight
        self.adjacency_matrix[to_vertex][from_vertex] = weight  # Неорієнтований граф

        self.adjacency_list[from_vertex].append((to_vertex, weight))
        self.adjacency_list[to_vertex].append((from_vertex, weight))

    def matrix_to_list(self):
        self.adjacency_list = {i: [] for i in range(self.vertex_count)}
        for i in range(self.vertex_count):
            for j in range(self.vertex_count):
                if self.adjacency_matrix[i][j] != 0:
                    self.adjacency_list[i].append((j, self.adjacency_matrix[i][j]))

    def list_to_matrix(self):
        self.adjacency_matrix = [[0] * self.vertex_count for _ in range(self.vertex_count)]
        for from_vertex, edges in self.adjacency_list.items():
            for to_vertex, weight in edges:
                self.adjacency_matrix[from_vertex][to_vertex] = weight

    def display_matrix(self):
        print("Adjacency Matrix:")
        for row in self.adjacency_matrix:
            print(row)

    def display_list(self):
        print("Adjacency List:")
        for vertex, edges in self.adjacency_list.items():
            print(f"{vertex}: {edges}")