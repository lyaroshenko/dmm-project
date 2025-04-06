import unittest
from graph import Graph
class TestGraph(unittest.TestCase):
    def setUp(self):
        self.graph = Graph(5)
        self.graph.add_edge(0, 1,10)
        self.graph.add_edge(1,2,15)
        self.graph.add_edge(2,3,20)
        self.graph.add_edge(3,4,25)
        self.graph.add_edge(4,0,30)
    def test_add_edge(self):
        expected_matrix = [
            [0, 10, 0, 0, 30],
            [10, 0, 15, 0, 0],
            [0, 15, 0, 20, 0],
            [0, 0, 20, 0, 25],
            [30, 0, 0, 25, 0]
        ]
        self.assertEqual(self.graph.adjacency_matrix, expected_matrix)
    def test_matrix_to_list(self):
        self.graph.matrix_to_list()
        expected_list = {
            0: [(1, 10), (4, 30)],
            1: [(0, 10), (2, 15)],
            2: [(1, 15), (3, 20)],
            3: [(2, 20), (4, 25)],
            4: [(0, 30), (3, 25)]
        }
        self.assertEqual(self.graph.adjacency_list, expected_list)
    def test_list_to_matrix(self):
        self.graph.matrix_to_list()
        self.graph.list_to_matrix()
        expected_matrix = [
            [0, 10, 0, 0, 30],
            [10, 0, 15, 0, 0],
            [0, 15, 0, 20, 0],
            [0, 0, 20, 0, 25],
            [30, 0, 0, 25, 0]
        ]
        self.assertEqual(self.graph.adjacency_matrix, expected_matrix)
    def test_display_matrix(self):
        import sys
        from io import StringIO

        captured_output = StringIO()
        sys.stdout = captured_output
        self.graph.display_matrix()
        sys.stdout = sys.__stdout__

        expected_output = (
            "Adjacency Matrix:\n"
            "[0, 10, 0, 0, 30]\n"
            "[10, 0, 15, 0, 0]\n"
            "[0, 15, 0, 20, 0]\n"
            "[0, 0, 20, 0, 25]\n"
            "[30, 0, 0, 25, 0]\n"
        )
        self.assertEqual(captured_output.getvalue(), expected_output)

    def test_display_list(self):
        import sys
        from io import StringIO

        captured_output = StringIO()
        sys.stdout = captured_output
        self.graph.matrix_to_list()
        self.graph.display_list()
        sys.stdout = sys.__stdout__

        expected_output = (
            "Adjacency List:\n"
            "0: [(1, 10), (4, 30)]\n"
            "1: [(0, 10), (2, 15)]\n"
            "2: [(1, 15), (3, 20)]\n"
            "3: [(2, 20), (4, 25)]\n"
            "4: [(0, 30), (3, 25)]\n"
        )
        self.assertEqual(captured_output.getvalue(), expected_output)

if __name__ == "__main__":
    unittest.main()