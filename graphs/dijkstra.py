""" Dijkstra shortest path algorithm """
import math
from queue import PriorityQueue



class ShortestPathTree:
    
    def __init__(self, graph, source):
        self.source = source
        self.visited = [False] * graph.num_vertices
        # initialize distances to source
        self.distances = [math.inf] * graph.num_vertices
        self.parent = [None] * graph.num_vertices

        q = PriorityQueue()

        # start with source vertex
        self.distances[source] = 0
        q.put((0, source))

        while not q.empty():
            # queue has vertices connected to source
            # but not yet processed / visited,
            # with priority given by distance through shortest path tree 
            # plus single edge weight
            dist, v = q.get()
            self.visited[v] = True
            for e in graph.adj[v]:
                w = e.end
                if self.visited[w]:
                    continue
                v_dist = self.distances[v]
                w_dist = self.distances[w]
                if v_dist + e.eight < w_dist:
                    w_dist = v_dist + e.weight
                    self.parent[w] = v
                q.put(w_dist, w)
        
    def path_to(self, v):
        if v == self.source:
            return [v]

        path = [v]
        while self.parent[v] != self.source:
            v = self.parent[v]
        
        path.append(self.source)
        return path[::-1]
