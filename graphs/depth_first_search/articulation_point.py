"""
Given a graph, find its articulation points, e.g. a point
whose removal increases the number of components of the
graph.
"""
from graphs.graph import create_graph


# pylint: disable=redefined-outer-name
class ArticulationPoints:
    def __init__(self, graph):
        """
        given adjacency representation of a graph

        returns list of articulation points
        """
        # current step of DFS
        self.step = 0
        # step number when visited
        # -1 means not visited
        self.visit_steps = [-1] * graph.num_vertices
        # earliest vertex in DFS a vertex is connected to
        self.earliest = [-1] * graph.num_vertices

    def depth_first_search(self, graph, u, v):
        """
        Through DFS, an articulation point v is found
        precisely when one of two conditions hold:

        1. v is a root vertex of the DFS tree and
           has more than one successor
        2. v is an interior vertex of the DFS tree
           and has a successor w such that:

              earliest(w) >= visit_step(v)
        """


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

    0, 9
    """
    graph = create_graph("graphs/data/tinyG.txt")
    ap = ArticulationPoints(graph)
