""" Dijkstra shortest path algorithm """
import math
from queue import PriorityQueue
from graphs.graph import create_weighted_digraph



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
            print(f'processing {v}')
            self.visited[v] = True
            for e in graph.adj[v]:
                w = e.end
                print(f'.. Checking edge to {w}')
                if self.visited[w]:
                    print('.... already processed... skipping')
                    continue
                v_dist = self.distances[v]
                w_dist = self.distances[w]
                if v_dist + e.weight < w_dist:
                    print(f'.... relaxing edge')
                    w_dist = v_dist + e.weight
                    self.distances[w] = w_dist
                    self.parent[w] = v
                q.put((w_dist, w))
        
    def path_to(self, v):
        if v == self.source:
            return [v]

        path = [v]
        while self.parent[v] != self.source:
            v = self.parent[v]
        
        path.append(self.source)
        return path[::-1]


if __name__ == '__main__':
    """
    Expected result:
    distances = [0, 1.05, 0.26, 0.9900000000000001, 0.38, 0.73, 1.5100000000000002, 0.6000000000000001]
    
    Example file and data from https://algs4.cs.princeton.edu/44sp/
    """
    graph = create_weighted_digraph('graphs/data/tinyEWD.txt')
    print(graph.adj)
    spt = ShortestPathTree(graph, 0)
    print(spt.distances)
