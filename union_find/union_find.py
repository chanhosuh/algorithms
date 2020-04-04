from abc import ABC


class UnionFind(ABC):
    """
    union-find data structure

    Each UnionFind instance maintains a collection of disjoint sets,
    called components.
    
    The items in each component are assumed to be integers and
    each is named by an arbitrary item in it.  
    
    find:
        returns a name for the set containing the given item.

    union:
        combines the components containing the two given items
    """

    def find(self, a):
        """ return the component id containing a """
        raise NotImplementedError()

    def union(self, a, b):
        """ combine the components containing a and b """
        raise NotImplementedError()

    def connected(self, a, b):
        """ return if a and b are in the same component """
        raise NotImplementedError()

    def count(self):
        """ return the number of components """
        raise NotImplementedError()
