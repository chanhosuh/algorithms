""" Dijkstra shortest path algorithm """
import math
from queue import PriorityQueue
from graphs.graph import create_weighted_digraph, DirectedEdge



class ShortestPathTree:
    
    def __init__(self, graph, source):
        self.source = source
        self.visited = [False] * graph.num_vertices
        # initialize distances to source
        self.distances = [math.inf] * graph.num_vertices
        self.edge_to = [None] * graph.num_vertices

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
                    self.edge_to[w] = e
                q.put((w_dist, w))
        
    def path_to(self, v):
        if v == self.source:
            return []

        e = self.edge_to[v]
        path = self.path_to(e.start)
        path.append(e)
        return path


if __name__ == '__main__':
    """
    Expected result:

    Distances:
    [0, 1.05, 0.26, 0.9900000000000001, 0.38, 0.73, 1.5100000000000002, 0.6000000000000001]
    Path to 1:
    [DirectedEdge(start=0 end=4 weight=0.38), DirectedEdge(start=4 end=5 weight=0.35), DirectedEdge(start=5 end=1 weight=0.32)]
    Path to 6:
    [DirectedEdge(start=0 end=2 weight=0.26), DirectedEdge(start=2 end=7 weight=0.34), DirectedEdge(start=7 end=3 weight=0.39), DirectedEdge(start=3 end=6 weight=0.52)]

    Example file from https://algs4.cs.princeton.edu/44sp/
    """
    graph = create_weighted_digraph('graphs/data/tinyEWD.txt')
    print(graph.adj)
    spt = ShortestPathTree(graph, 0)
    print('Distances:')
    print(spt.distances)
    print('Path to 1:')
    print(spt.path_to(1))
    print('Path to 6:')
    print(spt.path_to(6))
