from enum import nonmember

from numpy.matrixlib.defmatrix import matrix
from graph import Graph

def tsp_alg(graph) -> ([int], int ) :

    n = graph.vertex_count;
    matrix = graph.adjacency_matrix;

    # проверка на полноту
    # for i in range(n):
    #     for j in range(n):
    #         if matrix[i][j] == 0 and i != j :
    #             return False


    visited = []
    path: [int] = []

    total= 0
    current = 0

    visited.append(current)
    path.append(current)

    while len(visited) < n:
        min_weight = float('inf')
        next = None

        for j in range(n):
            if j not in visited and 0 < matrix[current][j] < min_weight:
                min_weight = matrix[current][j]
                next = j

        if not next : return [0], 0

        visited.append(next)
        path.append(next)
        total += min_weight
        # print(f'total: {total}')

        current = next

    path.append(path[0])
    total += matrix[current][path[0]]

    return (path, total)