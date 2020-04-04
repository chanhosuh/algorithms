"""
Given a graph, check its connectivity
"""


class ConnectedComponents:
    def __init__(self, graph):
        """
        given adjacency representation of a graph

        count:
            return number of components
        component_ids:
            return a vertex from each component
        components:
            return a list of vertices in each component
        """
        # visit status for each vertex
        self.visited = [False] * graph.num_vertices
        # component id for each vertex
        self.ids = list(range(graph.num_vertices))
        # number of components
        self.count = 0

        for v in graph.vertices:
            if self.visited[v]:
                continue

            self.depth_first_search(graph, v)
            self.count += 1

    def depth_first_search(self, graph, v):
        self.visited[v] = True
        self.ids[v] = self.count
        for w in graph.adj[v]:
            if self.visited[w]:
                continue
            self.depth_first_search(graph, w)

    @property
    def component_ids(self):
        return set(self.ids)

    @property
    def components(self):
        id_to_vertices = {}
        for i, id_ in enumerate(self.ids):
            id_to_vertices.setdefault(id_, []).append(i)
        return id_to_vertices
