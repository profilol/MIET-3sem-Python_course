import time
from math import fabs, sqrt
import random
import concurrent.futures

def process_matrix(q_j, p_i):
    return sqrt(fabs(q_j - p_i))

def generate_array(n):
    arr = []
    for i in range(n):
        arr.append(random.randint(0, 100))
    return arr

def initialize_matrix(n):
    return [[0 for i in range(n)] for j in range(n)]

def print_matrix(mtx):
    for row in mtx:
        for col in row:
            print(f"{col:.2f}", end=' ')
        print()


def process_row(q, p, row_num, n):
    row = []
    for i in range(n):
        r = process_matrix(q[i], p[row_num])
        row.append(r)
    return row

if __name__ == '__main__':
    N = 5000

    p = generate_array(N)
    q = generate_array(N)

    mtx1 = initialize_matrix(N)
    mtx2 = initialize_matrix(N)
    mtx3 = []

    start_without_concurrent = time.time()
    for i in range(N):
        for j in range(N):
            mtx1[i][j] = process_matrix(q[j], p[i])
    end_without_concurrent = time.time()

    with concurrent.futures.ProcessPoolExecutor() as executor:
        start_with_concurrent = time.time()
        rows = {executor.submit(process_row, q, p, i, N): i for i in range(N)}

    for future in concurrent.futures.as_completed(rows):
        row = rows[future]
        mtx2[row] = future.result()
    end_with_concurrent = time.time()

    print(f"Without concurrent: {end_without_concurrent - start_without_concurrent}")
    print(f"With concurrent: {end_with_concurrent - start_with_concurrent}")

    #print_matrix(mtx1)
    #print()
    #print_matrix(mtx2)