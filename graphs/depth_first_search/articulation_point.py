"""
Given a graph, find its articulation points, e.g. a point
whose removal increases the number of components of the
graph.
"""
from graphs.graph import create_graph
import math


# pylint: disable=redefined-outer-name
class ArticulationPoints:
    def __init__(self, graph):
        """
        Given adjacency list representation of a graph

        Return list of articulation points
        """
        # current step of DFS
        self.step = 0
        # step number when visited
        # -1 means not visited
        self.visit_steps = [-1] * graph.num_vertices
        # earliest vertex in DFS a vertex is connected to
        self.earliest = [math.inf] * graph.num_vertices

        self.articulation_points = []
        for u in graph.vertices:
            if self.visited(u):
                continue

            self.visit_steps[u] = self.step

            if len(graph.adj[u]) >= 2:
                self.articulation_points.append(u)

            for v in graph.adj[u]:
                self.depth_first_search(graph, v)

    def depth_first_search(self, graph, v):
        """
        Through DFS, an articulation point v is found
        precisely when one of two conditions hold:

        1. v is a root vertex of the DFS tree and
           has more than one successor
        2. v is an interior vertex of the DFS tree
           and has a successor w such that:

              earliest(w) >= visit_step(v)
        """
        self.step += 1
        self.visit_steps[v] = self.step
        for w in graph.adj[v]:
            if self.visited(w):
                self.earliest[v] = min(self.earliest[v], self.visit_steps[w])
                continue
            self.depth_first_search(graph, w)
            self.earliest[v] = min(self.earliest[v], self.earliest[w])

            if self.visit_steps[v] <= self.earliest[w]:
                self.articulation_points.append(v)

    def visited(self, v):
        return self.visit_steps[v] != -1


if __name__ == "__main__":
    # pylint: disable=pointless-string-statement
    r"""
    Graph looks like:

         0 ----------- 6     7 ---- 8
        /|\           /
       | | \         /
       | 1  2       /        9 ---- 10
       |           /         |\____
       | _ 3 __   /          |     \
       |/      \ /           11 --- 12
       5 ------ 4

    Expected result:
        [0, 9]
    """
    graph = create_graph("graphs/data/tinyG.txt")
    ap = ArticulationPoints(graph)
    print("Articulation points:", ap.articulation_points)
