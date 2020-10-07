import numpy as np
from graphviz import Digraph

from KOptimization import k1, k2, k3, k4
from NeimanMorgenstern import nm, check_inner_persistence, check_outer_persistence
from graph import Graph

from input import get_matrices


def get_graphs():
    # views = []
    graphs = []
    matrices = get_matrices()
    for k in range(10):
        view = Digraph('G', filename='hello' + str(k) + '.gv')
        g = Graph(15)
        matrix = matrices[k]
        for j in range(15):
            for i in range(15):
                if matrix[j][i] == 1:
                    g.addEdge(j, i)
                    view.edge(str(j), str(i))
        graphs.append(g)
    #     views.append(view)
    # views[1].view()
    return graphs


def check_cycle(graph):
    if graph.isCyclic() == 1:
        return 1
    else:
        return 0


graphs = get_graphs()
matrices = get_matrices()
for i in range(10):
    print("Graph: " + str(i))
    if check_cycle(graphs[i]) == 1:
        print("Cyclic")
        k1(matrices[i])
        k2(matrices[i])
        k3(matrices[i])
        k4(matrices[i])
    else:
        print("Acyclic")
        res = nm(matrices[i].T)
        print(str(res))
        print("Inner persistence: " + str(check_inner_persistence(matrices[i], res)))
        print("Outer persistence: " + str(check_outer_persistence(matrices[i], res)))