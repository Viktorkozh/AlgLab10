import heapq
import random


def print_ascending_sums(A, B):

    A.sort()
    B.sort()

    n = len(A)
    
    # Внешний цикл для каждого элемента из массива A
    for i in range(n):
        # Внутренний цикл для каждого элемента из массива B
        for j in range(n):
            print(A[i] + B[j], end=' ')


def fill_list(num_of_elements):
    a = [random.randint(0, 10) for _ in range(num_of_elements)]
    return a


A = fill_list(3)
B = fill_list(3)
print(sorted(A), "\n", sorted(B))
print_ascending_sums(A, B)
