class DepthFirstSearch(object):
    def __init__(self, graph):
        self.visited = [False] * graph.num_vertices
        self.graph = graph

    def search(self, vertex):
        self.visited[vertex] = True
        for v in self.graph.adj[vertex]:
            if not self.visited[v]:
                self.search(v)


DFS = DepthFirstSearch
