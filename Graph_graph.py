import numpy as np
import math
import matplotlib.pyplot as plt


class Graph:
    def __init__(self, num_vertices, edges):

        self.num_vertices = num_vertices
        self.Edges = edges
        self.num_edges = np.shape(edges)[0]

    def get_num_vertices(self):

        return self.num_vertices

    def get_num_edges(self):

        return self.num_edges

    def get_edges(self):

        return self.Edges

    def get_Euler_char(self):

        return self.num_vertices - self.num_edges

    def add_edge(self, head, tail):

        self.Edges.append([head, tail])

        self.num_edges += 1

    def delete_edge(self, head, tail):

        if [head, tail] in self.Edges:
            self.Edges.remove([head, tail])

            self.num_edges -= 1

    def add_vertex(self, num):

        self.num_vertices += 1

        for e in self.Edges:

            if e[0] >= num:
                e[0] += 1

            if e[1] >= num:
                e[1] += 1

    def delete_vertex(self, num):

        for e in self.Edges:

            if e[0] == num | e[1] == num:
                self.delete_edge(e[0], e[1])

            if e[0] > num:
                e[0] -= 1

            if e[1] > num:
                e[1] -= 1

        self.num_vertices -= 1

    def degree_of_vertex(self, vertex):

        in_deg = 0
        out_deg = 0

        for e in self.Edges:

            if e[0] == vertex:
                in_deg += 1

            if e[1] == vertex:
                out_deg += 1

        return [in_deg, out_deg]

    def adjacent_vertices(self, vertex):

        adj = []

        for e in self.Edges:

            if e[0] == vertex:
                adj.append(e[1])

            if e[1] == vertex:
                adj.append(e[0])

        return adj

    def is_adjacent(self, vertex1, vertex2):
        # If edge between vertex1 and vertex2 return edge.

        for e in self.Edges:

            if (e == [vertex1, vertex2]) | (e == [vertex2, vertex1]):
                return e

        return [-1, -1]

    def has_opposite(self, edge):

        for e in self.Edges:

            if edge == [e[1], e[0]]:
                return e

        return [-1, -1]

    def incidence_matrix(self):

        matrix = np.zeros((self.num_vertices, self.num_vertices))

        for e in self.Edges:
            matrix[e[0], e[1]] += 1

        return matrix

    def two_cells(self):
        # NOT CORRECT.  Does not get all the faces of a tetrahedron.
        two_cells = []
        marker = []

        for e in self.Edges:
            opposites = []

            adj0 = self.adjacent_vertices(e[0])
            adj1 = self.adjacent_vertices(e[1])

            for v in adj0:

                if v in adj1:
                    opposites.append(v)

            for w in opposites:

                if (w not in marker) | (e[0] not in marker) | (e[1] not in marker):
                    two_cells.append([e, self.is_adjacent(e[0], w), self.is_adjacent(e[1], w)])

                    marker.append(e[0])
                    marker.append(e[1])
                    marker.append(w)

        return two_cells

    def two_boundary_matrix(self):

        two_cells = self.two_cells()
        two_boundary_matrix = np.zeros((self.num_edges, np.shape(two_cells)[0]))

        for e in two_cells:
            two_boundary_matrix[self.Edges.index(e[0]), two_cells.index(e)] += 1
            two_boundary_matrix[self.Edges.index(e[1]), two_cells.index(e)] += -1
            two_boundary_matrix[self.Edges.index(e[2]), two_cells.index(e)] += 1

        return two_boundary_matrix

    # ==============================================================================
    #     calc_betti_nums:
    #     Input: E is a m-by-2 matrix, each row of which represents
    #     a directed edge in a graph with n verticies.
    #
    #     Function: Calculates the first, b0, and second, b1, betti numbers of the graph
    #     defined by E, and returns the ordered pair [b0,b1].
    # ==============================================================================

    def one_boundary_matrix(self):

        n = self.num_vertices
        m = self.num_edges
        edges = self.Edges
        matrix = np.zeros((n, m), dtype=int)

        for i in range(0, m):

            if edges[i][0] != edges[i][1]:
                matrix[edges[i][0], i] = 1
                matrix[edges[i][1], i] = -1

        return matrix

    def calc_betti_nums(self):

        n = self.num_vertices
        m = self.num_edges
        edges = self.Edges
        matrix = np.zeros((n, m), dtype=int)

        for i in range(0, m):

            if edges[i][0] != edges[i][1]:
                matrix[edges[i][0], i] = 1
                matrix[edges[i][1], i] = -1

        rk = np.linalg.matrix_rank(matrix)
        b0 = n - rk
        b1 = m - rk

        return [b0, b1]

    def draw_graph(self):

        n = self.num_vertices
        edges = self.Edges
        new_x = []
        new_y = []
        p = math.pi

        for i in range(n):
            new_x.append(math.cos(2 * p * i / n))
            new_y.append(math.sin(2 * p * i / n))

        plt.scatter(new_x, new_y)

        for e in edges:
            e0 = e[0]
            e1 = e[1]
            base_x = math.cos(2 * p * e1 / n)
            base_y = math.sin(2 * p * e1 / n)
            change_x = math.cos(2 * p * e0 / n) - math.cos(2 * p * e1 / n)
            change_y = math.sin(2 * p * e0 / n) - math.sin(2 * p * e1 / n)

            plt.arrow(base_x, base_y, change_x, change_y)

        plt.xlim(-1.1, 1.1)
        plt.ylim(-1.1, 1.1)

        plt.show()
