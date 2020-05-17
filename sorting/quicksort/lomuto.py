"""
A quicksort variation using Nico Lomuto's partitioning method,
as descrbed in Jon Bentley's "Programming Pearls", Chapter 11.

We tweak a refinement attributed to Sedgewick in Exercise 2,
so that no final swap of the pivot and comparison index is
needed, but we prefer to scan from left to right. ;)
"""
from sorting.quicksort.utils import position_pivot, shuffle, swap

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
    position_pivot(a, lo, hi)
    val = a[hi]
    p = lo - 1
    for i in range(lo, hi + 1):
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


if __name__ == "__main__":
    a = list(range(10000))
    shuffle(a)
    quicksort(a, 0, len(a) - 1)
    print(a)

    # This will throw
    # RecursionError: maximum recursion depth exceeded in comparison
    # See how this is handled in `fat_pivot.py`.
    a = [0] * 10000
    quicksort(a, 0, len(a) - 1)
