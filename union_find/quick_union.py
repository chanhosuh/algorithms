from union_find import UnionFind
from io import StringIO

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
        """
        while a != self.ids[a]:
            a = self.ids[a]
        return a

    def count(self):
        """ return the number of components """
        return self._count


if __name__ == "__main__":
    text = """10
        4 3
        3 8
        6 5
        9 4
        2 1
        8 9
        5 0
        7 2
        6 1
        1 0
        6 7"""
    buffer = StringIO(text)

    num_vertices = next(buffer)
    num_vertices = int(num_vertices.strip())
    union_find = QuickUnion(num_vertices)

    for line in buffer:
        print(line)
        a, b = line.split()
        a = int(a)
        b = int(b)
        union_find.union(a, b)

    print("number of components:", union_find.count())
    assert union_find.count() == 2
