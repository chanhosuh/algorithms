"""
Given a graph, check its connectivity
"""
from graphs.graph import create_graph


# pylint: disable=redefined-outer-name
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


if __name__ == "__main__":
    """
    Expected result:
    
    Number of components: 3
    Components with IDs:
    ID: 0
    Component: [0, 1, 2, 3, 4, 5, 6]

    ID: 1
    Component: [7, 8]

    ID: 2
    Component: [9, 10, 11, 12]
    """
    graph = create_graph("graphs/data/tinyG.txt")
    cc = ConnectedComponents(graph)
    print("Number of components:", cc.count)
    print("Components with IDs:")
    for id_, component in cc.components.items():
        print("ID:", id_)
        print("Component:", component)
        print("")
