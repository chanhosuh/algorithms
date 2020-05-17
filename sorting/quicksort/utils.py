from random import randrange


def position_pivot(a, lo, hi):
    """
    various possibilities, but here we select a reasonably
    robust pivot selection methodology: median of three

    After possibly several swaps, a[hi] is the "median"
    value of a[lo], a[hi-1], a[hi].

    Note:
    - it's assumed lo < hi
    """
    m = hi - 1
    if a[hi] > a[m]:
        swap(a, hi, m)
    if a[lo] > a[m]:
        swap(a, lo, m)
    if a[hi] < a[lo]:
        swap(a, hi, lo)


def swap(a, i, j):
    a[i], a[j] = a[j], a[i]


def shuffle(a):
    for i in reversed(range(len(a))):
        n = randrange(i + 1)
        swap(a, n, i)


def print_head(a, num=10):
    """ print head of the list only """
    print(a[:num] + ["..."])


def is_sorted(a):
    last = None
    for x in a:
        if last and last > x:
            return False
        last = x
    return True


def print_if_sorted(a):
    if is_sorted(a):
        print("**** List is sorted ****")
    else:
        print("**** List is NOT sorted ****")
    print_head(a)
