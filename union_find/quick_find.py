from .union_find import UnionFind


class QuickFind(UnionFind):
    def __init__(self, num_vertices):
        self.num_vertices = num_vertices
        self.ids = list(range(num_vertices))

    def union(self, a, b):
        """
        combine the components containing a and b
        
        for each k connected to b, set its id to 
        the component id for a
        """
        id_b = self.ids[b]
        id_a = self.ids[a]
        for k, id_ in enumerate(self.ids):
            if id_ == id_b:
                self.ids[k] = id_a

    def find(self, a):
        """ return the component id containing a """
        return self.ids[a]

    def connected(self, a, b):
        """ return if a and b are in the same component """
        return self.find(a) == self.find(b)

    def count(self):
        """ return the number of components """
        return len(set(self.ids))
