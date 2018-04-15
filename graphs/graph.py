'''
Adjency-list representation of a graph
'''


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
    '''
        Text file should consist of integers in the format:
        3   <-- number of vertices
        2   <-- number of edges
        0 2   <-- vertices of edge
        2 1   <-- vertices of edge
    '''
    with open(text_file, 'rb') as f:
        num_vertices = f.next()
        num_edges = f.next()
        graph = Graph(num_vertices)
        for edge in f:
            v1, v2 = edge.split()
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
