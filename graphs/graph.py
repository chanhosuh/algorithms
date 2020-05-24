"""
Adjacency list representation of a graph
"""


class Graph(object):
    def __init__(self, num_vertices):
        self.num_vertices = num_vertices
        self.vertices = range(num_vertices)
        self.adj = {}
        for v in self.vertices:
            self.adj[v] = []

    def add_edge(self, v, w):
        self.adj[v].append(w)
        self.adj[w].append(v)


def create_graph(text_file):
    """
        Text file should consist of integers in the format:
        3   <-- number of vertices
        2   <-- number of edges
        0 2   <-- vertices of edge
        2 1   <-- vertices of edge
    """
    with open(text_file, "r") as f:
        num_vertices = next(f)
        num_vertices = int(num_vertices.strip())
        # num_edges, unused
        _ = next(f)
        graph = Graph(num_vertices)
        for edge in f:
            v1, v2 = edge.split()
            v1 = int(v1)
            v2 = int(v2)
            graph.add_edge(v1, v2)

    return graph


class EdgeWeightedDiGraph(object):
    def __init__(self, num_vertices):
        self.num_vertices = num_vertices
        self.vertices = range(num_vertices)
        self.adj = {}
        for v in self.vertices:
            self.adj[v] = []

    def add_edge(self, start, end, weight):
        e = DirectedEdge(start, end, weight)
        self.adj[start].append(e)


class DirectedEdge(object):
    def __init__(self, start, end, weight):
        self.start = start
        self.end = end
        self.weight = weight

    def __repr__(self):
        return f"DirectedEdge(start={self.start}, end={self.end}, weight={self.weight})"


def create_weighted_digraph(text_file):
    """
        Text file should consist of integers in the format:
        3   <-- number of vertices
        2   <-- number of edges
        0 2 0.10   <-- directed edge: start, end, weight
        2 1 1.2   <-- directed edge: start, end, weight
    """
    with open(text_file, "r") as f:
        num_vertices = next(f)
        num_vertices = int(num_vertices.strip())
        # num_edges, unused
        _ = next(f)
        graph = EdgeWeightedDiGraph(num_vertices)
        for edge in f:
            v1, v2, weight = edge.split()
            v1 = int(v1)
            v2 = int(v2)
            weight = float(weight)
            graph.add_edge(v1, v2, weight)

    return graph
