import Graph_graph
import numpy as np


class GraphGenerator:

    def __init__(self, num_vertices, num_edges):
        self.num_vertices = num_vertices
        self.num_edges = num_edges
        self.Edges = self.generate_edges()
        self.graph = Graph_graph.Graph(self.num_vertices, self.Edges)

    def get_graph(self):

        return self.graph

    def generate_edges(self):
        all_edges = []
        for i in range(self.num_vertices):
            for j in range(i + 1, self.num_vertices):
                if i != j:
                    all_edges.append([i, j])
        ind = np.random.choice(range(np.shape(all_edges)[0]), self.num_edges, replace=False)
        e = [all_edges[i] for i in ind]

        return e
