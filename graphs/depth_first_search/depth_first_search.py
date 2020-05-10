class DepthFirstSearch(object):
    def __init__(self, graph):
        self.visited = [False] * graph.num_vertices
        
        for v in graph.vertices:
            if not self.visited[v]:
                continue
            self.search(v)

    def search(self, vertex):
        self.visited[vertex] = True
        for v in self.graph.adj[vertex]:
            if self.visited[v]:
                continue
            self.search(v)


DFS = DepthFirstSearch
