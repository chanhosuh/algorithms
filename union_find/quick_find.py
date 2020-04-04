from union_find import UnionFind
from io import StringIO

# pylint: disable=redefined-outer-name
class QuickFind(UnionFind):
    def __init__(self, num_vertices):
        self.num_vertices = num_vertices
        self.ids = list(range(num_vertices))

        self._count = num_vertices

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

        self._count -= 1

    def find(self, a):
        """ return the component id containing a """
        return self.ids[a]

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
    union_find = QuickFind(num_vertices)

    for line in buffer:
        print(line)
        a, b = line.split()
        a = int(a)
        b = int(b)
        union_find.union(a, b)

    print("number of components:", union_find.count())
    assert union_find.count() == 2
