"""
In Jon Bentley, "Programming Pearls", Chapter 11, exercise 11,
it is suggested to use a "fat pivot" invariant.  Presumably,
this is to handle the issue with many duplicates equal to the
pivot value that occurs with the Lomuto method.
"""
from .utils import position_pivot, print_if_sorted, random_list, shuffle, swap


# pylint: disable=redefined-outer-name


def quicksort(a, lo, hi):
    """
    Args:
        a (list): list to be sorted
        lo: valid index in a
        hi: valid index in a
    """
    if lo >= hi:
        return

    p, q = partition(a, lo, hi)
    quicksort(a, lo, p)
    quicksort(a, q, hi)


def partition(a, lo, hi):
    """
    Args:
        a (list): list to be partitioned
        lo: valid index in a
        hi: valid index in a

    Returns:
        p, q:
            two indices, bounding an open interval
            which contains elements equal to the pivot
            value

            The pivot element is in a correct, sorted
            position.  This is key to the termination
            of quicksort, as we know each partition
            step makes progress.
    """
    position_pivot(a, lo, hi, pivot=lo)
    val = a[lo]
    p = lo - 1
    q = hi + 1
    i = lo + 1
    while i < q:
        # invariant:
        #  a[lo..p] < val
        #  a[p+1..i-1] == val
        #  a[q..hi] > val
        #
        #       <       =       ?           >
        #  |---------|-----|---------|----------|
        #  lo       p       i         q        hi
        #
        if a[i] < val:
            p += 1
            swap(a, p, i)
            i += 1
        elif a[i] > val:
            q -= 1
            swap(a, q, i)
        else:
            i += 1

    # The invariant implies:
    #
    #    a[i] < val for i <= p
    #    a[i] == val for p < i < q
    #    a[i] > val for i > q
    #
    return p, q


if __name__ == "__main__":
    print("Testing distinct values...")
    a = list(range(10000))
    shuffle(a)
    quicksort(a, 0, len(a) - 1)
    print_if_sorted(a)

    print("Testing all values are the same...")
    a = [0] * 10000
    quicksort(a, 0, len(a) - 1)

    print("Testing uniform number of duplicates...")
    a = list(range(200)) * 50
    for i in range(10):
        print("Run:", i)
        shuffle(a)
        quicksort(a, 0, len(a) - 1)
        print_if_sorted(a)

    print("Testing random arrays with small keys...")
    for i in range(50):
        print("Run:", i)
        a = random_list(10000, 50)
        quicksort(a, 0, len(a) - 1)
        print_if_sorted(a)

    print("Testing random arrays with large keys...")
    for i in range(50):
        print("Run:", i)
        a = random_list(100000, 10000)
        quicksort(a, 0, len(a) - 1)
        print_if_sorted(a)

# TODO:
# let's do some doubling tests to see that we really do have
# an O(n log n) quicksort implementation
