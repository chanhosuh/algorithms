import contextlib
from io import StringIO
import sys
import time


@contextlib.contextmanager
def get_data():

    try:
        filepath = sys.argv[1]
        buffer = open(filepath, "r")
        yield buffer
    except IndexError:
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
        yield buffer

    finally:
        buffer.close()


def run_harness(union_find):
    start = time.process_time()

    with get_data() as buffer:
        num_vertices = next(buffer)
        num_vertices = int(num_vertices.strip())
        union_find = union_find(num_vertices)

        for line in buffer:
            a, b = line.split()
            a = int(a)
            b = int(b)
            union_find.union(a, b)

    elapsed_time = time.process_time() - start

    print("number of components:", union_find.count())
    print("elapsed time:", elapsed_time)
