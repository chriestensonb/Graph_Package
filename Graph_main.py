import Graph_generate
import matplotlib.pyplot as plt
import numpy as np


class Main:

    def __init__(self, num_graphs, num_vertices, num_edges, make_hist):
        self.num_graphs = num_graphs
        self.num_vertices = num_vertices
        self.num_edges = num_edges
        self.make_hist = make_hist
        b0, b1 = self.simulation()
        if self.make_hist:
            self.visualize(b0, 'Connected Components')
            self.visualize(b1, 'Cycles')
        else:
            pass

        self.b = [b0, b1]

    def simulation(self):
        b0 = []
        b1 = []

        for i in range(self.num_graphs):
            g = Graph_generate.GraphGenerator(self.num_vertices, self.num_edges).get_graph()

            b0.append(g.calc_betti_nums()[0])
            b1.append(g.calc_betti_nums()[1])

        return b0, b1

    @staticmethod
    def visualize(b, title):
        upper = max(b)
        lower = min(b)
        bins = (upper - lower)

        plt.hist(b, bins=bins, normed=True)
        plt.xlim(0, upper + 1)
        plt.xlabel(title)
        plt.show()

    def get_data(self):
        return np.array(self.b)
