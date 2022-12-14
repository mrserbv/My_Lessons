
# Методы сортировки массивов

import random


def create_rand_list(length):
    new_list = []
    for _ in range(length):
        new_list.append(random.randint(1, length))
    return new_list


def insert_sort(A):
    """ Сортировка списка A вставками"""
    N = len(A)
    for top in range(1, N):
        k = top
        while k > 0 and A[k-1] > A[k]:
            A[k], A[k-1] = A[k-1], A[k]
            k -= 1


def choise_sort(A):
    """ Сортировка списка A выбором"""
    N = len(A)
    for pos in range(0, N-1):
        for k in range(pos+1, N):
            if A[k] < A[pos]:
                A[k], A[pos] = A[pos], A[k]


def buble_sort(A):
    """ Сортировка списка A методом пузырька"""
    N = len(A)
    for bypass in range(1, N):
        for k in range(0, N-bypass):
            if A[k] > A[k+1]:
                A[k], A[k+1] = A[k+1], A[k]


def sort_test(sort_algoritm):
    print('Тестируем: ', sort_algoritm.__doc__)
    print('Testcase #1: ', end='')
    A = [4, 2, 5, 1, 3]
    A_sorted = [1, 2, 3, 4, 5]
    sort_algoritm(A)
    print('OK' if A == A_sorted else 'Fail')

    print('Testcase #2: ', end='')
    A = list(range(10, 20)) + list(range(0, 10))
    A_sorted = list(range(20))
    sort_algoritm(A)
    print('OK' if A == A_sorted else 'Fail')

    print('Testcase #2: ', end='')
    A = [4, 2, 4, 2, 1]
    A_sorted = [1, 2, 2, 4, 4]
    sort_algoritm(A)
    print('OK' if A == A_sorted else 'Fail')


if __name__ == '__main__':
    sort_test(insert_sort)
    sort_test(choise_sort)
    sort_test(buble_sort)
