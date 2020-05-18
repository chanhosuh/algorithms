"""
In Jon Bentley, "Programming Pearls", Chapter 11, exercise 11,
it is suggested to use a "fat pivot" invariant.  Presumably,
this is to handle the issue with many duplicates equal to the
pivot value that occurs with the Lomuto method.
"""
from .lomuto import shuffle, position_pivot, swap
from sorting.quicksort.utils import print_if_sorted, random_list

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
            and everything above is ">=".

            The pivot element is in a correct, sorted
            position.  This is key to the termination
            of quicksort, as we know each partition
            step makes progress.
    """
    position_pivot(a, lo, hi)
    val = a[hi]
    p = q = lo - 1
    for i in range(lo, hi + 1):
        # invariant:
        #  a[0..p] < val
        #  a[p+1..q] == val
        #  a[q+1..i-1] > val
        #
        #       <       =       >           ?
        #  |---------|-----|---------|----------|
        #  lo       p     q           i        hi
        #
        if a[i] == val:
            q += 1
            swap(a, q, i)
        elif a[i] < val:
            p += 1
            swap(a, p, i)
            q += 1
            if a[i] == val:
                swap(a, q, i)

    # Last iteration must swap a[q] with a[hi]
    # which means a[q] = val.  Together with the
    # invariant, this means:
    #
    #    a[i] < a[q] for i <= p
    #    a[i] == a[q] for p < i <= q
    #    a[i] > a[q] for i > q
    #
    # Return the average index of equal vals
    # to avoid unbalanced partitioning
    return ((p + 1) + q) // 2


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
