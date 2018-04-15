

class DepthFirstSearch(object):

    def __init__(self, graph):
        self.marked = [False] * graph.num_vertices
        self.graph = graph

    def search(self, vertex):
        self.marked[vertex] = True
        for v in self.graph.adj[vertex]:
            if not self.marked[v]:
                self.search(v)

