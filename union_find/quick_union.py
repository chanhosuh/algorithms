from union_find import UnionFind
from union_find.utils import run_harness

# pylint: disable=redefined-outer-name
class QuickUnion(UnionFind):
    def __init__(self, num_vertices):
        self.num_vertices = num_vertices
        self.ids = list(range(num_vertices))

        self._count = num_vertices

    def union(self, a, b):
        """
        combine the components containing a and b
        
        Algorithm:
        
        1. use "find" to get the root ids for the
           component trees for a and b
        2. link the root id for a to root id for b 
        3. decrement count
        
        Runtime complexity of this algorithm is
        2 * "find" complexity + constant.
        """
        root_id_a = self.find(a)
        root_id_b = self.find(b)

        if root_id_a == root_id_b:
            return

        self.ids[root_id_a] = root_id_b

        self._count -= 1

    def find(self, a):
        """
        return the root id for the component tree
        containing a

        Algorithm:
        
        1. follow links, starting from a until
           you reach a self-link, i.e. an item
           linking to itself
        2. return self-link
        
        Runtime complexity is O(log k) where k is
        the number of items in the component tree
        for a.
        """
        while a != self.ids[a]:
            a = self.ids[a]
        return a

    def count(self):
        """ return the number of components """
        return self._count


if __name__ == "__main__":
    run_harness(QuickUnion)
