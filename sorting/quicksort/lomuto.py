"""
A quicksort variation using Nico Lomuto's partitioning method,
as descrbed in Jon Bentley's "Programming Pearls", Chapter 11.

We tweak a refinement attributed to Sedgewick in Exercise 2,
so that no final swap of the pivot and comparison index is
needed, but we prefer to scan from left to right. ;)
"""


def quicksort(a, lo, hi):
    """
    Args:
        a (list): list to be sorted
        lo: valid index in a
        hi: valid index in a
    """
    if lo >= hi:
        return

    
    p = partition(a, lo, hi)
    quicksort(a, lo, p - 1)
    quicksort(a, p + 1, hi)
    
    
    
def partition(a, lo, hi):
    """
    Args:
        a (list): list to be partitioned
        lo: valid index in a
        hi: valid index in a
    
    Returns:
        int:
            "pivot" index, everything below is "<="
            and everything above is ">".
            
            The pivot element is in a correct, sorted
            position.  This is key to the termination
            of quicksort, as we know each partition
            step makes progress.
    """
    val = a[hi]
    p = lo - 1
    for i in range(lo, hi+1):
        # invariant:
        #  a[0..p] <= val
        #  a[p+1..i-1] > val
        #
        #     <=        >         ?
        #  |---------|------|----------|  
        #  lo       p        i        hi
        #
        if a[i] <= val:
            p += 1
            swap(a, p, i)
    
    # Last iteration must swap a[p] with a[hi]
    # which means a[p] = val.  Together with the
    # invariant, this means:
    #
    #    a[i] <= a[p] for i < p
    #    a[j] > a[p] for j > p
    #
    return p


def swap(a, i, j):
    a[i], a[j] = a[j], a[i]

def shuffle(a): 
    from random import randrange
    for i in reversed(range(len(a))):
        n = randrange(i + 1)
        swap(a, n, i)
        
    
    
# if __name__ == '__main__':
a = list(range(100))
shuffle(a)
quicksort(a, 0, len(a)-1)
print(a)
