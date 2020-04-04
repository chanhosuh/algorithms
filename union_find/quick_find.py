from union_find import UnionFind
from union_find.utils import run_harness

# pylint: disable=redefined-outer-name
class QuickFind(UnionFind):
    def __init__(self, num_vertices):
        self.num_vertices = num_vertices
        self.ids = list(range(num_vertices))

        self._count = num_vertices

    def union(self, a, b):
        """
        combine the components containing a and b
        
        Algorithm:
        
        1. for each k connected to b, set its id to 
           the component id for a
        2. decrement count
        
        Note: this is O(M*N) for M = num_vertices
        and N = number of connections, but "find"
        is very fast, O(1).
        """
        id_b = self.ids[b]
        id_a = self.ids[a]

        if id_a == id_b:
            return

        for k, id_ in enumerate(self.ids):
            if id_ == id_b:
                self.ids[k] = id_a

        self._count -= 1

    def find(self, a):
        """ return the component id containing a """
        return self.ids[a]

    def count(self):
        """ return the number of components """
        return self._count


if __name__ == "__main__":
    run_harness(QuickFind)
