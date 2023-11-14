import math

print('hello world')
A = [2, 3, 4]
B = [7, -3, 2, 3]


def sum_list(a: list, b: list):
    summed_list: list = []

    a_size = len(a)
    b_size = len(b)

    for indice in range(max(a_size, b_size)):
        a_value = a[indice] if indice <= a_size - 1 else 0
        b_value = b[indice] if indice <= b_size - 1 else 0

        summed_list.append(a_value + b_value)

    return summed_list

print(sum_list(A, B))