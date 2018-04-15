class Heap(object):

    def __init__(self):
        self.array = [None, ]  # start indexing at 1
        self.size = 0  # number of elements in heap

    def __swap(self, i, j):
        tmp = self.array[i]
        self.array[i] = self.array[j]
        self.array[j] = tmp

    def _sink(self, k):
        while 2*k <= self.size:
            j = 2*k
            if j + 1 <= self.size and self.array[j + 1] < self.array[j]:
                j += 1
            if self.array[k] > self.array[j]:
                self.__swap(k, j)
                k = j
            else:
                break

    def _swim(self, k):
        while k > 1 and self.array[k/2] > self.array[k]:
            self.__swap(k, k/2)
            k /= 2

    def insert(self, val):
        ''' append val to end of array and
            swim val up '''
        self.array.append(val)
        self.size += 1
        self._swim(self.size)

    def min(self):
        if len(self.array) <= 1:
            raise RuntimeError('No element in heap.')
        self.__swap(1, self.size)
        val = self.array.pop()
        self.size -= 1
        self._sink(1)
        return val


class IndexedHeap(object):

    def __init__(self):
        self.array = [None, ]  # start indexing at 1
        self.size = 0  # number of elements in heap

    def __swap(self, i, j):
        tmp = self.array[i]
        self.array[i] = self.array[j]
        self.array[j] = tmp

    def _sink(self, k):
        while 2*k <= self.size:
            j = 2*k
            if j + 1 <= self.size and self.array[j + 1] < self.array[j]:
                j += 1
            if self.array[k] > self.array[j]:
                self.__swap(k, j)
                k = j
            else:
                break

    def _swim(self, k):
        while k > 1 and self.array[k/2] > self.array[k]:
            self.__swap(k, k/2)
            k /= 2

    def insert(self, index, val):
        ''' append val to end of array and
            swim val up '''
        self.array.append(val)
        self.size += 1
        self._swim(self.size)

    def update(self, index, val):
        pass
    
    def contains(self, index):
        pass
    
    def delete(self, index):
        pass
    
    def min_index(self):
        pass

    def min(self):
        if len(self.array) <= 1:
            raise RuntimeError('No element in heap.')
        self.__swap(1, self.size)
        val = self.array.pop()
        self.size -= 1
        self._sink(1)
        return val
